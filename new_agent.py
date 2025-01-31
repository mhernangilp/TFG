import ollama

body = """                 Dear customer,    You have received this email because we believe your Apple ID has been recently compromise.You are required to verify your information.Click the link below and sign in using your Apple ID and password to start the process.  Verify here >   Thanks, Apple Customer Support          TM and copyright  2015 Apple Inc. 1 Infinite Loop, MS 96-DM, Cupertino, CA 95014. All Rights Reserved Keep Informed Privacy Policy <A style=""LINE-HEIGHT: 1.34em; FONT-FAMILY: Geneva, Verdana, Arial, Helvetica, sans-serif; COLOR: rgb(153,153,153); FONT-SIZE: 9px; TEXT-DECORATION: underline"" target=_blank #?="""">My Apple ID     <HTML><head><meta http-equiv=""Content-Type"" content=""text/html; charset=iso-8859-1""/></head><BODY><P> <TABLE style=""WIDOWS: 1; TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; MARGIN: 0px auto; FONT: 13px arial, sans-serif; WHITE-SPACE: normal; LETTER-SPACING: normal; COLOR: rgb(34,34,34); WORD-SPACING: 0px; -webkit-text-stroke-width: 0px; font-stretch: normal"" border=0 cellSpacing=0 cellPadding=0 width=648 bgColor=#ffffff align=center> <TBODY> <TR> <TD style=""MARGIN: 0px; FONT-FAMILY: arial, sans-serif""><IMG style=""MARGIN: 0px; DISPLAY: block"" border=0 alt="""" src=""http://images.apple.com/dm/misc/notification1/top.gif"" width=648 height=122></TD></TR></TBODY></TABLE> <TABLE style=""WIDOWS: 1; TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(241,241,241); TEXT-INDENT: 0px; MARGIN: 0px auto; FONT: 13px arial, sans-serif; WHITE-SPACE: normal; LETTER-SPACING: normal; COLOR: rgb(34,34,34); WORD-SPACING: 0px; -webkit-text-stroke-width: 0px; font-stretch: normal"" border=0 cellSpacing=0 cellPadding=0 width=630 align=center> <TBODY> <TR> <TD style=""MARGIN: 0px; FONT-FAMILY: arial, sans-serif""> <TABLE style=""BACKGROUND-COLOR: rgb(241,241,241); MARGIN: 0px auto"" border=0 cellSpacing=0 cellPadding=0 width=490 align=center> <TBODY> <TR> <TD style=""PADDING-BOTTOM: 22px; MARGIN: 0px; PADDING-LEFT: 0px; PADDING-RIGHT: 0px; FONT-FAMILY: arial, sans-serif; PADDING-TOP: 0px"" width=490 align=left> <DIV style=""LINE-HEIGHT: 1.25em; FONT-FAMILY: 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', Arial, Helvetica, Verdana, sans-serif; COLOR: rgb(51,51,51); FONT-SIZE: 12px""><SPAN style=""FONT-WEIGHT: bold"">Dear customer,</SPAN><BR><BR><SPAN class=Apple-converted-space>&nbsp; You have received this email because we believe your Apple ID has been recently compromise.You are required to verify your information.</SPAN><SPAN style=""TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(241,241,241); TEXT-INDENT: 0px; DISPLAY: inline !important; FONT: 12px/15px 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', Arial, Helvetica, Verdana, sans-serif; WHITE-SPACE: normal; FLOAT: none; LETTER-SPACING: normal; COLOR: rgb(51,51,51); WORD-SPACING: 0px; -webkit-text-stroke-width: 0px; font-stretch: normal"">Click the link below and sign in using your Apple ID and password to start the process.<BR></SPAN><BR><A style=""COLOR: rgb(0,136,204); TEXT-DECORATION: none"" id=yui_3_16_0_1_1422051245475_61938 href=""http://www.digitalcrops.co.uk/a"" rel=nofollow target=_blank>Verify here &gt;</A></DIV> <DIV style=""LINE-HEIGHT: 1.25em; FONT-FAMILY: 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', Arial, Helvetica, Verdana, sans-serif; COLOR: rgb(51,51,51); FONT-SIZE: 12px"">&nbsp;</DIV> <DIV style=""LINE-HEIGHT: 1.25em; FONT-FAMILY: 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', Arial, Helvetica, Verdana, sans-serif; COLOR: rgb(51,51,51); FONT-SIZE: 12px"">Thanks,<BR>Apple Customer Support</DIV></TD></TR></TBODY></TABLE></TD></TR> <TR> <TD style=""MARGIN: 0px; FONT-FAMILY: arial, sans-serif; PADDING-TOP: 101px""><IMG style=""MARGIN: 0px; DISPLAY: block"" border=0 alt="""" src=""http://images.apple.com/dm/misc/notification1/btm.gif"" width=630 height=21></TD></TR></TBODY></TABLE> <TABLE style=""WIDOWS: 1; TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; MARGIN: 0px auto; FONT: 13px arial, sans-serif; WHITE-SPACE: normal; LETTER-SPACING: normal; COLOR: rgb(34,34,34); WORD-SPACING: 0px; -webkit-text-stroke-width: 0px; font-stretch: normal"" border=0 cellSpacing=0 cellPadding=0 width=490 align=center> <TBODY> <TR> <TD style=""PADDING-BOTTOM: 10px; MARGIN: 0px; PADDING-LEFT: 0px; PADDING-RIGHT: 20px; FONT-FAMILY: arial, sans-serif; PADDING-TOP: 10px""> <DIV style=""LINE-HEIGHT: 1.34em; FONT-FAMILY: Geneva, Verdana, Arial, Helvetica, sans-serif; COLOR: rgb(153,153,153); FONT-SIZE: 9px"">TM and copyright&nbsp; 2015 Apple Inc.<SPAN class=Apple-converted-space>&nbsp;</SPAN><SPAN class=Apple-converted-space><A style=""TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; FONT: 9px/12px Geneva, Verdana, Arial, Helvetica, sans-serif; WHITE-SPACE: normal; LETTER-SPACING: normal; COLOR: rgb(153,153,153); WORD-SPACING: 0px; TEXT-DECORATION: none; -webkit-text-stroke-width: 0px; font-stretch: normal"" href="""">1 Infinite Loop, MS 96-DM, Cupertino, CA 95014</A><SPAN style=""TEXT-TRANSFORM: none; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; DISPLAY: inline !important; FONT: 9px/12px Geneva, Verdana, Arial, Helvetica, sans-serif; WHITE-SPACE: normal; FLOAT: none; LETTER-SPACING: normal; COLOR: rgb(153,153,153); WORD-SPACING: 0px; -webkit-text-stroke-width: 0px; font-stretch: normal"">.<BR></SPAN></SPAN><A style=""COLOR: rgb(153,153,153); TEXT-DECORATION: underline"" href=""file:///C:/Users/Administrator/AppData/Local/Temp/2/tmpbivysg.html#"" target=_blank>All Rights Reserved</A>&nbsp;<A style=""LINE-HEIGHT: 1.34em; FONT-FAMILY: Geneva, Verdana, Arial, Helvetica, sans-serif; COLOR: rgb(153,153,153); FONT-SIZE: 9px; TEXT-DECORATION: underline"" href=""file:///C:/Users/Administrator/AppData/Local/Temp/2/tmpbivysg.html#"" target=_blank>Keep Informed</A>&nbsp;<A style=""LINE-HEIGHT: 1.34em; FONT-FAMILY: Geneva, Verdana, Arial, Helvetica, sans-serif; COLOR: rgb(153,153,153); FONT-SIZE: 9px; TEXT-DECORATION: underline"" href=""file:///C:/Users/Administrator/AppData/Local/Temp/2/tmpbivysg.html#"" target=_blank>Privacy Policy</A>&nbsp;<A style=""LINE-HEIGHT: 1.34em; FONT-FAMILY: Geneva, Verdana, Arial, Helvetica, sans-serif; COLOR: rgb(153,153,153); FONT-SIZE: 9px; TEXT-DECORATION: underline"" target=_blank #?="""">My Apple ID</A></DIV></TD></TR> <TR> <TD style=""MARGIN: 0px; FONT-FAMILY: arial, sans-serif""><IMG src=""http://outsideapple.apple.com/img/APPLE_EMAIL_LINK/spacer4.gif?v=2&amp;a=k%2BmjWPCFEH1m5ry2zndhAoTpdPJnoOKW9vF1PDhfunstevZAKgvTXvAx%2FKBT0NwWFxioI1y6gMVKzygsLP9l498FZOU6Z73eM1CavjrDXnyIsuRAHQeMAZSRvJ7tQB9nHcdStacc1oWImWW5ZFPQpztpICCoV1cjzB87WyR7p93OBGwhfYSWxxTJwomPw0QVUyyb5iNNV0v1gPnFKm6OCy7RPi0tOHboiibPP3TQj%2B1DVvQwsB%2FuoN3x08SeLJyVuZZR6oXTcR6UQuaqLFg9duuylrDCFnSfcAYHzIme26NV424ur77xg4rUhjI3OwJOviwH0UmehH9Io11gTmil0CoVC9e2CZbPy1nYR1Gnl7g%3D""></TD></TR></TBODY></TABLE></P></BODY></HTML>"""

prompt = body + """ #### Assess the given email body line for potential phishing characteristics.  
For each of the following factors, return a JSON object where each factor is a boolean (true or false) indicating whether the body line exhibits that characteristic:

1. **Urgency and Threats**: Does the body line create a sense of urgency or threaten the recipient in any way?  
2. **Suspicious Keywords**: Does the body line contain words like "URGENT", "ACTION REQUIRED", "UPDATE NEEDED", "SECURITY ALERT", "SECURITY UPDATE", or similar phishing-related terms?  
3. **Generic Language**: Does the body line use generic greetings like "Dear User" or "Hello Customer"?  
4. **Lack of Personalization**: Is the body line addressed to a generic recipient rather than a specific name or email address?  
5. **Request for Sensitive Information**: Does the body line ask for personal identifiable information (PII), login credentials, or financial data?  

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

Here are some expamples on how to answer:

Input: "Your account has been suspended. Immediate action required!"
Output:
"{
  "urgency_and_threats": true,
  "suspicious_keywords": true,
  "generic_language": false,
  "lack_of_personalization": true,
  "request_for_sensitive_info": false
}"

Input: "Hello valued customer, please verify your billing details now."
Output:
"{
  "urgency_and_threats": false,
  "suspicious_keywords": true,
  "generic_language": true,
  "lack_of_personalization": true,
  "request_for_sensitive_info": true
}"

Input: "John, your recent purchase receipt is attached."
Output:
"{
  "urgency_and_threats": false,
  "suspicious_keywords": false,
  "generic_language": false,
  "lack_of_personalization": false,
  "request_for_sensitive_info": false
}"

"""

response = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    options={"temperature": 0.12}
)

print(response["message"]["content"])