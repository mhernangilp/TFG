import os
import email
import re
from collections import defaultdict
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def parse_email(raw_email):
    msg = email.message_from_string(raw_email)
    headers = {key: msg[key] for key in msg.keys()}
    body = ""
    try:
        if msg.is_multipart():
            body = ''.join([part.get_payload(decode=True).decode('utf-8', errors='ignore') if part.get_payload(decode=True) else '' for part in msg.get_payload()])
        else:
            payload = msg.get_payload(decode=True)
            body = payload.decode('utf-8', errors='ignore') if payload else ""
    except Exception as e:
        print(f"Error decoding email body: {e}")
    return headers, body

def extract_main_type(content_type):
    """Extrae solo el main_type del Content-Type, ignorando charset y otros parámetros."""
    if not content_type:
        return None
    return content_type.split(";")[0].strip()

def clean_from_field(from_field):
    """Extrae solo la dirección de correo del campo From."""
    if not from_field:
        return None
    # Buscar dirección de correo en formato estándar con regex
    match = re.search(r'<([^>]+)>', from_field)
    if match:
        return match.group(1).strip()
    # Si no hay formato estándar, verificar si el campo es una dirección de correo
    elif re.match(r'^[^@]+@[^@]+\.[^@]+$', from_field.strip()):
        return from_field.strip()
    return None

def load_emails_from_folder(folder_path, multi_email_file=False, label=0):
    emails = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            email_content = file.read()
            if multi_email_file:
                for raw_email in email_content.split('\n\nFrom '):
                    if raw_email.strip():
                        headers, body = parse_email("From " + raw_email.strip())
                        # Curar el campo From
                        if "From" in headers:
                            headers["From"] = clean_from_field(headers["From"])
                        # Estándar de fecha (si existe)
                        if "Date" in headers:
                            date_tuple = parsedate_tz(headers["Date"])
                            if date_tuple:
                                timestamp = mktime_tz(date_tuple)
                                standardized_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                                headers["Date"] = standardized_date
                        # Curar Content-Type
                        if "Content-Type" in headers:
                            headers["Content-Type"] = extract_main_type(headers["Content-Type"])
                        emails.append((headers, body, label))
            else:
                headers, body = parse_email(email_content)
                # Curar el campo From
                if "From" in headers:
                    headers["From"] = clean_from_field(headers["From"])
                # Estándar de fecha (si existe)
                if "Date" in headers:
                    date_tuple = parsedate_tz(headers["Date"])
                    if date_tuple:
                        timestamp = mktime_tz(date_tuple)
                        standardized_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                        headers["Date"] = standardized_date
                # Curar Content-Type
                if "Content-Type" in headers:
                    headers["Content-Type"] = extract_main_type(headers["Content-Type"])
                emails.append((headers, body, label))
    return emails

# Carpetas de emails de phishing y de Enron
phishing_folder_path = '/home/marky/TFG/resources/raw_data/phishing'
enron_folder_path = '/home/marky/TFG/resources/raw_data/enron'

# Cargar emails de ambas carpetas con su respectiva etiqueta
phishing_emails = load_emails_from_folder(phishing_folder_path, multi_email_file=True, label=1)
enron_emails = load_emails_from_folder(enron_folder_path, multi_email_file=False, label=0)
all_emails = phishing_emails + enron_emails


# Función para calcular el número de caracteres no alfanuméricos en la dirección de email
def calculate_non_alphanumeric_count(email_address):
    if not email_address:
        return 0
    return sum(1 for c in email_address if not c.isalnum())

# Crear contadores para phishing y no phishing
phishing_counts = Counter()
non_phishing_counts = Counter()

# Rango de números de caracteres no alfanuméricos (0-5, 5-10, ...)
ranges = [(i, i + 1) for i in range(0, 21, 1)]

# Función para asignar un número a un tramo
def get_range(count):
    for lower, upper in ranges:
        if lower <= count < upper:
            return f"{lower}-{upper}"
    return f"{ranges[-1][1]}+"

# Procesar emails y clasificar en tramos
for headers, body, label in all_emails:
    from_field = headers.get("From")
    if from_field:
        count = calculate_non_alphanumeric_count(from_field)
        range_label = get_range(count)
        if label == 1:
            phishing_counts[range_label] += 1
        else:
            non_phishing_counts[range_label] += 1

# Ordenar los tramos para el gráfico
sorted_ranges = [f"{lower}-{upper}" for lower, upper in ranges[:-1]] + [f"{ranges[-1][1]}+"]
phishing_values = [phishing_counts[range_label] for range_label in sorted_ranges]
non_phishing_values = [non_phishing_counts[range_label] for range_label in sorted_ranges]

# Configurar el gráfico
x = np.arange(len(sorted_ranges))  # Posiciones para las etiquetas del eje x
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, non_phishing_values, width, label='No Phishing (Label 0)', color='blue')
rects2 = ax.bar(x + width/2, phishing_values, width, label='Phishing (Label 1)', color='red')

# Añadir etiquetas y título
ax.set_xlabel('Número de Caracteres No Alfanuméricos en el Campo From')
ax.set_ylabel('Número de Correos')
ax.set_title('Distribución de Caracteres No Alfanuméricos en Direcciones de Email')
ax.set_xticks(x)
ax.set_xticklabels(sorted_ranges, rotation=45)
ax.legend()

# Añadir etiquetas encima de las barras
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                f'{int(height)}', ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# Mostrar el gráfico
plt.tight_layout()
plt.show()