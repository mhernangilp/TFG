import csv
import ollama

csv.field_size_limit(10**6)

# Calcular valor con media
def get_average_response(prompt, model="llama3.1:8b", n=5):
    results = []
    for _ in range(n):
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        try:
            results.append(int(response["message"]["content"]))
        except ValueError:
            raise ValueError(f"El modelo devolvió una respuesta no válida: {response['message']['content']}")
    average = round(sum(results) / len(results))
    return average

# Procesar un archivo CSV
def process_csv(input_file, output_file):
    i = 0
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for row in reader:
            subject = row['subject']
            body = row['body']

            try:
                # Comprobar si subject y body son enteros
                subject_score = int(subject)
                body_score = int(body)
                
                # Validar que los valores están en el rango esperado
                if not (0 <= subject_score <= 4) or not (0 <= body_score <= 4):
                    print(f"Warning: subject or body not in range in row {i}. Values: subject={subject}, body={body}")
                
                # Copiar la fila tal cual si ya está procesada
                writer.writerow(row)

            except ValueError:
                # Generar prompts para subject y body si no están procesados
                prompt_subject = f"""{subject} #### Assess the given email subject line for potential phishing 
                characteristics. Consider the following factors and assign a score from 0 
                to 4, where:

                0 (Not Phishy): The subject line appears legitimate, with no 
                suspicious language or keywords.
                1 (Somewhat Suspicious): The subject line exhibits some red flags, 
                but they can be easily explained as minor mistakes or oversights.
                2 (Moderately Phishy): The subject line displays several warning 
                signs of a phishing attempt, such as generic greetings, poor grammar, or 
                suspicious keywords.
                3 (Likely Phishing): The subject line contains multiple, obvious red 
                flags, including threats, demands for sensitive information, or malicious 
                links.
                4 (Somewhat Credible): The subject line may appear legitimate at 
                first glance but has some inconsistencies that suggest it might be a 
                phishing attempt. Further investigation is needed to determine its 
                authenticity.

                Consider the following factors when classifying the email subject 
                line:

                1. Urgency and Threats: Does the subject line create a sense of 
                urgency or threaten the recipient in any way?
                2. Suspicious Keywords: Are there keywords such as "URGENT", "ACTION 
                REQUIRED", "UPDATE NEEDED", "SECURITY ALERT", or other similar phrases 
                that are commonly used in phishing attempts?
                3. Generic Language: Does the subject line use generic language, such 
                as greetings like "Dear User" or "Hello Customer"?
                4. Lack of Personalization: Is the subject line addressed to a generic 
                recipient, rather than the specific individual\'s name or email address?
                5. Request for Sensitive Information: Does the subject line ask for 
                personal identifiable information (PII), login credentials, or financial 
                data?

                Evaluate each factor and assign scores from 0 to 4 based on your 
                assessment.

                Once you have evaluated all factors, sum up the scores and convert them to 
                a final classification between 0 (Not Phishy) and 4 (Very Phishy).

                Give me ONLY the final number, nothing else"""

                prompt_body = f"""{body} #### Assess the given email body for potential phishing characteristics. 
                Consider the following factors and assign a score from 0 to 4, where:

                0 (Not Phishy): The email appears legitimate, with no suspicious 
                language or requests.
                1 (Somewhat Suspicious): The email exhibits some red flags, but they 
                can be easily explained as minor mistakes or oversights.
                2 (Moderately Phishy): The email displays several warning signs of a 
                phishing attempt, such as generic greetings, poor grammar, or suspicious 
                links.
                3 (Likely Phishing): The email contains multiple, obvious red flags, 
                including threats, demands for sensitive information, or malicious 
                attachments.
                4 (Somewhat Credible): The email may appear legitimate at first 
                glance but has some inconsistencies that suggest it might be a phishing 
                attempt. Further investigation is needed to determine its authenticity.

                Consider the following factors when classifying the email body:

                1. Generic Language and Lack of Personalization: Does the email use 
                generic language, such as greetings like "Dear User" or "Hello Customer", 
                and lack personalized elements?
                2. Requests for Sensitive Information: Does the email ask for personal 
                identifiable information (PII), login credentials, or financial data?
                3. Urgency and Threats: Does the email create a sense of urgency or 
                threaten the recipient in any way?
                4. Suspicious Links or Attachments: Are there links that lead to 
                unfamiliar websites, or attachments from unknown sources? Note: In cases 
                where URLs have been modified for privacy (e.g., "jose@monkey.org"), 
                consider this when evaluating suspicious links.
                5. Poor Grammar and Spelling: Does the email contain numerous 
                grammatical errors, spelling mistakes, or awkward phrasing?

                Special note on URL modifications: When evaluating links in the email 
                body, keep in mind that URLs may have been modified to protect sensitive 
                information (e.g., "jose@monkey.org" instead of a real email address). 
                This modification should not affect your assessment of the link's 
                legitimacy.

                Evaluate each factor and assign scores from 0 to 4 based on your 
                assessment.

                Once you have evaluated all factors, sum up the scores and convert them to 
                a final classification between 0 (Not Phishy) and 4 (Very Phishy).

                Give me ONLY the final number, nothing else"""

                # Obtener respuestas de la LLM
                try:
                    temp_s = get_average_response(prompt_subject)
                    temp_b = get_average_response(prompt_body)
                    
                    if not (0 <= int(temp_s) <= 4):
                        raise ValueError(f"Subject response out of range: {temp_s}")
                    if not (0 <= int(temp_b) <= 4):
                        raise ValueError(f"Body response out of range: {temp_b}")
                    
                    row['subject'] = temp_s
                    row['body'] = temp_b
                except Exception as e:
                    print(f"Error procesando fila: {row}. Error: {e}")
                    writer.writerow(row)
                    i += 1
                    continue  # Saltar fila en caso de error

                # Escribir fila procesada en el nuevo archivo
                writer.writerow(row)
                print(f'Processing row {i}, with new subject={row["subject"]} and body={row["body"]}')

            i += 1

# Archivo de entrada y salida
input_csv = 'resources/processed_data/testing_output7.csv'
output_csv = 'resources/processed_data/testing_output8.csv'

process_csv(input_csv, output_csv)
print(f"Procesamiento completado. Resultados guardados en {output_csv}.")
