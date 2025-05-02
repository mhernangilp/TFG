import csv
import ollama
import re
import json

csv.field_size_limit(10**8)

def validate_json_format(response):
    # Regex para capturar el bloque JSON en el formato esperado
    pattern = r'\{\s*"urgency_and_threats"\s*:\s*(true|false),\s*"suspicious_keywords"\s*:\s*(true|false),\s*"generic_language"\s*:\s*(true|false),\s*"lack_of_personalization"\s*:\s*(true|false),\s*("request_for_sensitive_info"|"too_good_to_be_true")\s*:\s*(true|false)\s*\}'
    
    match = re.search(pattern, response)
    
    if match:
        try:
            # Convertimos el match a un objeto JSON
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    else:
        print("Response does not match the expected format.")
        return None


# Calcular valor con media
def get_response(prompt):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0.1}
    )
    try:
        response_json = validate_json_format(response["message"]["content"])
        print(response["message"]["content"])
        count = sum(value for value in response_json.values())
        
    except ValueError:
        raise ValueError(f"El modelo devolvió una respuesta no válida: {response['message']['content']}")
    return count

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

                # Copiar la fila tal cual si ya está procesada
                writer.writerow(row)
                print(f"Fila {i} ya procesada")

            except ValueError:
                # Generar prompts para subject y body si no están procesados
                prompt_subject = """
                    ### Assess the given email subject line for potential phishing characteristics  

                    <EMAIL_SUBJECT>  
                    """ + subject + """  
                    </EMAIL_SUBJECT>  

                    For each of the following factors, return a JSON object where each factor is a boolean (`true` or `false`) indicating whether the subject line exhibits that characteristic. Do **NOT** include any explanations, Python code, or comments. Return only the JSON object.  

                    #### Factors to Check:  
                    1. **Urgency and Threats** (Does the subject create a sense of urgency or fear to provoke immediate action?)  
                    2. **Suspicious Keywords** (Does the subject contain common phishing-related words like "urgent," "payment," "account locked," etc.?)  
                    3. **Generic Language** (Is the subject vague or applicable to anyone, rather than being specific?)  
                    4. **Lack of Personalization** (Does the subject avoid using a name or other specific identifiers that a legitimate sender would use?)  
                    5. **Too Good to Be True** (Does the subject promise an unrealistic benefit, like winning a prize or receiving unexpected money?)  

                    ### Expected Output Format:  
                    Return **only** a JSON object with the following structure—no explanations, comments, or additional text. If the output contains anything other than a JSON object, the response is incorrect.  

                    ```json  
                    {  
                    "urgency_and_threats": true/false,  
                    "suspicious_keywords": true/false,  
                    "generic_language": true/false,  
                    "lack_of_personalization": true/false,  
                    "too_good_to_be_true": true/false  
                    }  
                    ```  

                    ### Examples:  

                    Input: "URGENT: Your account will be closed soon!"  
                    Output:  
                    {  
                    "urgency_and_threats": true,  
                    "suspicious_keywords": true,  
                    "generic_language": false,  
                    "lack_of_personalization": true,  
                    "too_good_to_be_true": false  
                    }  

                    Input: "Congratulations! You've won a free iPhone!"  
                    Output:  
                    {  
                    "urgency_and_threats": false,  
                    "suspicious_keywords": true,  
                    "generic_language": true,  
                    "lack_of_personalization": true,  
                    "too_good_to_be_true": true  
                    }  

                    Input: "John, your flight itinerary is ready."  
                    Output:  
                    {  
                    "urgency_and_threats": false,  
                    "suspicious_keywords": false,  
                    "generic_language": false,  
                    "lack_of_personalization": false,  
                    "too_good_to_be_true": false  
                    }  

                    ### Important:  
                    Return only the JSON object. No explanations, reasoning, or additional content should be provided.  
                    """

                prompt_body = """
                    ### Assess the given email body line for potential phishing characteristics

                    <EMAIL_BODY>
                    """ + body + """
                    </EMAIL_BODY>

                    For each of the following factors, return a JSON object where each factor is a boolean (`true` or `false`) indicating whether the body line exhibits that characteristic. Do **NOT** include any explanations, Python code, or comments. Return only the JSON object.

                    #### Factors to Check:
                    1. **Urgency and Threats**
                    2. **Suspicious Keywords**
                    3. **Generic Language**
                    4. **Lack of Personalization**
                    5. **Request for Sensitive Information**

                    ### Expected Output Format:
                    Return **only** a JSON object with the following structure—no explanations, comments, or additional text. If the output contains anything other than a JSON object, the response is incorrect.

                    ```json
                    {
                    "urgency_and_threats": true/false,
                    "suspicious_keywords": true/false,
                    "generic_language": true/false,
                    "lack_of_personalization": true/false,
                    "request_for_sensitive_info": true/false
                    }

                    ### Examples:

                    Input: "Your account has been suspended. Immediate action required!"
                    Output:
                    {
                    "urgency_and_threats": true,
                    "suspicious_keywords": true,
                    "generic_language": false,
                    "lack_of_personalization": true,
                    "request_for_sensitive_info": false
                    }

                    Input: "Hello valued customer, please verify your billing details now."
                    Output:
                    {
                    "urgency_and_threats": false,
                    "suspicious_keywords": true,
                    "generic_language": true,
                    "lack_of_personalization": true,
                    "request_for_sensitive_info": true
                    }

                    Input: "John, your recent purchase receipt is attached."
                    Output:
                    {
                    "urgency_and_threats": false,
                    "suspicious_keywords": false,
                    "generic_language": false,
                    "lack_of_personalization": false,
                    "request_for_sensitive_info": false
                    }

                    ### Important:
                    Return only the JSON object. No explanations, reasoning, or additional content should be provided.
                    """

                # Obtener respuestas de la LLM
                try:
                    temp_s = get_response(prompt_subject)
                    temp_b = get_response(prompt_body)
                    
                    row['subject'] = temp_s
                    row['body'] = temp_b
                except Exception as e:
                    print(f"Error procesando fila: {i}. Error: {e}")
                    writer.writerow(row)
                    i += 1
                    continue  # Saltar fila en caso de error

                # Escribir fila procesada en el nuevo archivo
                writer.writerow(row)
                print(f'Processing row {i}')

            i += 1

# Archivo de entrada y salida
input_csv = 'resources/processed_data/emails.csv'
output_csv = 'resources/processed_data/dataset2.csv'

process_csv(input_csv, output_csv)
print(f"Procesamiento completado. Resultados guardados en {output_csv}.")
