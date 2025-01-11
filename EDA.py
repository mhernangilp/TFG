import os
import email
import pandas as pd
from collections import defaultdict

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
                        emails.append((headers, body, label))
            else:
                headers, body = parse_email(email_content)
                emails.append((headers, body, label))
    return emails

def get_common_attributes(emails, threshold=0.6):
    attribute_counts = defaultdict(int)
    total_emails = len(emails)
    
    # Contar la frecuencia de cada atributo en los encabezados
    for headers, _, _ in emails:
        for attribute in headers:
            attribute_counts[attribute] += 1
    
    # Calcular el umbral en base al porcentaje especificado
    min_count = total_emails * threshold
    common_attributes = {attr for attr, count in attribute_counts.items() if count >= min_count}
    
    return common_attributes

# Carpetas de emails de phishing y de Enron
phishing_folder_path = '/home/marky/TFG/resources/raw_data/phishing'
enron_folder_path = '/home/marky/TFG/resources/raw_data/enron'

# Cargar emails de ambas carpetas con su respectiva etiqueta
phishing_emails = load_emails_from_folder(phishing_folder_path, multi_email_file=True, label=1)
enron_emails = load_emails_from_folder(enron_folder_path, multi_email_file=False, label=0)
all_emails = phishing_emails + enron_emails

# Obtener atributos comunes que están presentes en el 60% de los correos
common_attributes = get_common_attributes(all_emails, threshold=1)

for headers, body, label in all_emails:
    filtered_headers = {key: headers.get(key, None) for key in common_attributes}
    filtered_headers['body'] = body
    filtered_headers['is_phishing'] = label
    print(filtered_headers)

print(f"Dataset guardado en {output_csv_path}")