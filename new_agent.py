import ollama

subject = "-Temporary information confirmed-"

prompt = subject + """ #### Assess the given email subject line for potential phishing characteristics.  
For each of the following factors, return a JSON object where each factor is a boolean (true or false) indicating whether the subject line exhibits that characteristic:

1. **Urgency and Threats**: Does the subject line create a sense of urgency or threaten the recipient in any way?  
2. **Suspicious Keywords**: Does the subject line contain words like "URGENT", "ACTION REQUIRED", "UPDATE NEEDED", "SECURITY ALERT", or similar phishing-related terms?  
3. **Generic Language**: Does the subject line use generic greetings like "Dear User" or "Hello Customer"?  
4. **Lack of Personalization**: Is the subject line addressed to a generic recipient rather than a specific name or email address?  
5. **Request for Sensitive Information**: Does the subject line ask for personal identifiable information (PII), login credentials, or financial data?  

### Expected Output Format:
Return ONLY a JSON object with the following structure:
```json
{
  "urgency_and_threats": true/false,
  "suspicious_keywords": true/false,
  "generic_language": true/false,
  "lack_of_personalization": true/false,
  "request_for_sensitive_info": true/false
}
"""

response = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    options={"temperature": 0.12}
)

print(response["message"]["content"])