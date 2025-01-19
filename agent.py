import ollama

# Calcular valor con frecuencia
def get_consistent_response(prompt, model="llama3.1:8b", n=5):
    results = []
    for _ in range(n):
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        results.append(response["message"]["content"])
    return max(set(results), key=results.count)

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

subject = "Here goes de subject"
body = "Here goes the body"

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

print("Generating subject response ...")
consistent_response = get_average_response(prompt_subject)
print(consistent_response)


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

print("Generating body response ...")
consistent_response = get_average_response(prompt_body)
print(consistent_response)