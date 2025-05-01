import os
import email
import re
from collections import defaultdict
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
import csv

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
                emails.append((headers, body, label))
    return emails

# Carpetas de emails de phishing y de Enron
phishing_folder_path = './resources/raw_data/phishing'
enron_folder_path = './resources/raw_data/enron'

# Cargar emails de ambas carpetas con su respectiva etiqueta
phishing_emails = load_emails_from_folder(phishing_folder_path, multi_email_file=True, label=1)
enron_emails = load_emails_from_folder(enron_folder_path, multi_email_file=False, label=0)
all_emails = phishing_emails + enron_emails


def calculate_uppercase_percentage(email_address):
    if not email_address:
        return None
    uppercase_count = sum(1 for c in email_address if c.isupper())
    lowercase_count = sum(1 for c in email_address if c.islower())
    if lowercase_count == 0:
        return 0  # Evitar división por cero
    return (uppercase_count / (uppercase_count + lowercase_count)) * 100

# Función para calcular el número de caracteres no alfanuméricos en la dirección de email
def calculate_non_alphanumeric_count(email_address):
    if not email_address:
        return 0
    return sum(1 for c in email_address if not c.isalnum())

def save_emails_to_csv(emails, output_path):
    with open(output_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Escribir encabezados
        writer.writerow([
            "num_chars_from",
            "special_chars_from",
            "uppercase_percentage_from",
            "date",
            "subject",
            "body",
            "label"
        ])

        for headers, body, label in emails:
            # Extraer valores
            from_field = headers.get("From")
            num_chars_from = len(from_field) if from_field else "NULL"

            uppercase_percentage_from = (
                calculate_uppercase_percentage(from_field)
                if from_field else "NULL"
            )

            special_chars_from = (
                calculate_non_alphanumeric_count(from_field)
                if from_field else "NULL"
            )

            date = headers.get("Date", "NULL")

            subject = headers.get("Subject", "NULL")

            body_text = body if body else "NULL"

            # Escribir fila
            writer.writerow([
                num_chars_from,
                uppercase_percentage_from,
                special_chars_from,
                date,
                subject,
                body_text.replace('\n', ' ').replace('\r', ' '),  # Sustituir saltos de línea
                label
            ])

# Ruta de salida para el archivo CSV
output_csv_path = './resources/processed_data/emails.csv'

# Guardar todos los emails en formato CSV
save_emails_to_csv(all_emails, output_csv_path)

print(f"Emails guardados en {output_csv_path}")