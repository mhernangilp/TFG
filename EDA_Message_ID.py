import os
import email
import re
from collections import defaultdict
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

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


# Extraer características del email (número de caracteres en el Message-ID)
def extract_email_features(headers, label):
    message_id = headers.get("Message-ID", "")
    num_chars = len(message_id) if message_id else 0
    return {'num_chars': num_chars, 'label': label}

# Extraer las características de los emails
features = [extract_email_features(headers, label) for headers, _, label in all_emails]

# Crear un DataFrame para facilitar el análisis
df = pd.DataFrame(features)

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['num_chars'], df['label'], c=df['label'], cmap='coolwarm', alpha=0.6)

plt.title("Relación entre la longitud del Message-ID y si es phishing")
plt.xlabel("Longitud del Message-ID")
plt.ylabel("Phishing (1) / No Phishing (0)")
plt.grid(True)
plt.show()