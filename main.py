import os
import email

def parse_email(raw_email):
    msg = email.message_from_string(raw_email)
    headers = {key: msg[key] for key in msg.keys()}
    body = ""
    try:
        if msg.is_multipart():
            # Filtrar y decodificar las partes del cuerpo que no son None
            body = ''.join([part.get_payload(decode=True).decode('utf-8', errors='ignore') if part.get_payload(decode=True) else '' for part in msg.get_payload()])
        else:
            payload = msg.get_payload(decode=True)
            body = payload.decode('utf-8', errors='ignore') if payload else ""
    except Exception as e:
        print(f"Error decoding email body: {e}")
    return headers, body

def load_emails_from_folder(folder_path, multi_email_file=False):
    emails = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                email_content = file.read()
                if multi_email_file:
                    for raw_email in email_content.split('\n\nFrom '):  # Separador típico en archivos MBOX
                        if raw_email.strip():  # Evita procesar bloques vacíos
                            headers, body = parse_email("From " + raw_email.strip())
                            emails.append((headers, body))
                else:
                    headers, body = parse_email(email_content)
                    emails.append((headers, body))
        except PermissionError as e:
            print(f"Permission denied for file: {file_path}")
            exit(1)
    return emails

# Carpetas de emails de phishing y de Enron
phishing_folder_path = 'C:/Users/marky/OneDrive/Escritorio/TFG/resources/test/phishing'
enron_folder_path = 'C:/Users/marky/OneDrive/Escritorio/TFG/resources/test/enron'

# Cargar emails de ambas carpetas
phishing_emails = load_emails_from_folder(phishing_folder_path, multi_email_file=True)
enron_emails = load_emails_from_folder(enron_folder_path, multi_email_file=False)

# Mostrar headers de los emails
for headers, body in phishing_emails + enron_emails:
    print(headers)
