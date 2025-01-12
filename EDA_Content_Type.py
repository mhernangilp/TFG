import os
import email
from collections import defaultdict
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
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

# Agrupar por Content-Type y etiqueta
content_type_counts = defaultdict(lambda: [0, 0])  # [no_phishing_count, phishing_count]

for headers, _, label in all_emails:
    content_type = headers.get("Content-Type", "Unknown")
    content_type_counts[content_type][label] += 1

# Preparar datos para el gráfico
content_types = list(content_type_counts.keys())
no_phishing_counts = [counts[0] for counts in content_type_counts.values()]
phishing_counts = [counts[1] for counts in content_type_counts.values()]

# Crear el gráfico
x = range(len(content_types))
width = 0.4

plt.figure(figsize=(12, 6))
plt.bar(x, no_phishing_counts, width=width, label='No Phishing', color='green')
plt.bar([i + width for i in x], phishing_counts, width=width, label='Phishing', color='red')

# Etiquetas y título
plt.xlabel('Content-Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Emails by Content-Type and Phishing Status', fontsize=14)
plt.xticks([i + width / 2 for i in x], content_types, rotation=45, ha='right')
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
