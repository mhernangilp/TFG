import ollama

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

subject = "Congrats! You've Been Selected For Netflix Reward"
body = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.=
w3.org/TR/html4/loose.dtd">

<html><head>
<meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">
<meta name=3D"GENERATOR" content=3D"MSHTML 11.00.10570.1001"></head>
<body style=3D"margin: 0.5em;">
<table style=3D"width: 531px; color: rgb(38, 40, 42); text-transform: none;=
 letter-spacing: normal; font-family: &quot;Helvetica Neue&quot;, Helvetica=
, Arial, sans-serif; font-size: 13px; font-style: normal; font-weight: 400;=
 word-spacing: 0px; vertical-align: top; white-space: normal; border-collap=
se: collapse; min-height: 100%; orphans: 2; widows: 2; font-variant-ligatur=
es: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text=
-decoration-thickness: initial; text-decoration-style:=20
initial; text-decoration-color: initial;" cellspacing=3D"0" cellpadding=3D"=
0">
<tbody>
<tr>
<td style=3D"margin: 0px; width: 531px; font-family: &quot;Google Sans&quot=
;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top;"=
>
<div style=3D"margin: 0px auto; max-width: 630px;">
<table style=3D"width: 531px; color: rgb(38, 40, 42); text-transform: none;=
 letter-spacing: normal; font-family: &quot;Helvetica Neue&quot;, Helvetica=
, Arial, sans-serif; font-size: 13px; font-style: normal; font-weight: 400;=
 word-spacing: 0px; vertical-align: top; white-space: normal; border-collap=
se: collapse; min-height: 100%; orphans: 2; widows: 2; font-variant-ligatur=
es: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text=
-decoration-thickness: initial; text-decoration-style:=20
initial; text-decoration-color: initial;" cellspacing=3D"0" cellpadding=3D"=
0"><tbody><tr><td style=3D"margin: 0px; width: 531px; font-family: &quot;Go=
ogle Sans&quot;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertica=
l-align: top;"><div style=3D"margin: 0px auto; max-width: 630px;">
<table style=3D"width: 531px; color: rgb(38, 40, 42); text-transform: none;=
 letter-spacing: normal; font-family: &quot;Helvetica Neue&quot;, Helvetica=
, Arial, sans-serif; font-size: 13px; font-style: normal; font-weight: 400;=
 word-spacing: 0px; vertical-align: top; white-space: normal; border-collap=
se: collapse; min-height: 100%; orphans: 2; widows: 2; font-variant-ligatur=
es: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text=
-decoration-thickness: initial; text-decoration-style:=20
initial; text-decoration-color: initial;" cellspacing=3D"0" cellpadding=3D"=
0"><tbody><tr><td style=3D"margin: 0px; width: 531px; font-family: &quot;Go=
ogle Sans&quot;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertica=
l-align: top;"><div style=3D"margin: 0px auto; max-width: 630px;"><table st=
yle=3D"width: 531px; font-family: &quot;Helvetica Neue&quot;, Helvetica, Ar=
ial, sans-serif; vertical-align: top; border-collapse: collapse; min-height=
: 100%;" cellspacing=3D"0" cellpadding=3D"0"><tbody><tr>
<td style=3D"margin: 0px; width: 531px; font-family: &quot;Google Sans&quot=
;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top;"=
><div style=3D"margin: 0px auto; width: 519px; height: 251px; max-width: 63=
0px;">
<table style=3D"width: 531px; color: rgb(38, 40, 42); text-transform: none;=
 letter-spacing: normal; font-family: &quot;Helvetica Neue&quot;, Helvetica=
, Arial, sans-serif; font-size: 13px; font-style: normal; font-weight: 400;=
 word-spacing: 0px; vertical-align: top; white-space: normal; border-collap=
se: collapse; min-height: 100%; orphans: 2; widows: 2; font-variant-ligatur=
es: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text=
-decoration-thickness: initial; text-decoration-style:=20
initial; text-decoration-color: initial;" cellspacing=3D"0" cellpadding=3D"=
0"><tbody><tr><td style=3D"margin: 0px; width: 531px; font-family: &quot;Go=
ogle Sans&quot;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertica=
l-align: top;"><div style=3D"margin: 0px auto; max-width: 630px;"><table st=
yle=3D"width: 531px; font-family: &quot;Helvetica Neue&quot;, Helvetica, Ar=
ial, sans-serif; vertical-align: top; border-collapse: collapse; min-height=
: 100%;" cellspacing=3D"0" cellpadding=3D"0"><tbody><tr>
<td style=3D"margin: 0px; width: 531px; font-family: &quot;Google Sans&quot=
;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top;"=
><div style=3D"margin: 0px auto; max-width: 630px;"><table style=3D"width: =
531px; font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-seri=
f; vertical-align: top; border-collapse: collapse; min-height: 100%;" cells=
pacing=3D"0" cellpadding=3D"0"><tbody><tr>
<td style=3D"margin: 0px; width: 531px; font-family: &quot;Google Sans&quot=
;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top;"=
><div style=3D"margin: 0px auto; max-width: 630px;"><table style=3D"width: =
531px; font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-seri=
f; vertical-align: top; border-collapse: collapse; min-height: 100%;" cells=
pacing=3D"0" cellpadding=3D"0"><tbody><tr>
<td style=3D"margin: 0px; width: 531px; font-family: &quot;Google Sans&quot=
;, Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top;"=
><div style=3D"margin: 0px auto; width: 519px; height: 251px; max-width: 63=
0px;"><div style=3D"color: rgb(44, 54, 58); font-family: Roboto, sans-serif=
; font-size: 14px; border-top-color: currentColor; border-top-width: 0px; b=
order-top-style: none; box-sizing: border-box; background-color: rgb(244, 2=
48, 245);">
<div style=3D"width: 591px; height: 24px; padding-top: 5px; padding-right: =
5px; padding-bottom: 5px; margin-left: 18px; border-top-color: currentColor=
; border-top-width: 0px; border-top-style: none; float: left; box-sizing: b=
order-box;"><div style=3D'font-family: wf_segoe-ui_normal, "Segoe UI", "Seg=
oe WP", Tahoma, Arial, sans-serif; font-size: 13px; border-top-color: curre=
ntColor; border-top-width: 0px; border-top-style: none; box-sizing: border-=
box;'><span style=3D"box-sizing: border-box;">
<font size=3D"2"><br class=3D"gmail-Apple-interchange-newline"><br>Message =
generated from&nbsp;<span>&nbsp;</span><a style=3D"color: rgb(17, 85, 204);=
" href=3D"http://angelshipco.com/" target=3D"_blank">monkey.org</a>&nbsp;so=
urce.</font></span></div></div><div style=3D"box-sizing: border-box;"><div =
style=3D"width: 5px; height: 30px; border-top-color: currentColor; border-t=
op-width: 0px; border-top-style: none; box-sizing: border-box; background-c=
olor: rgb(86, 166, 89);"></div></div></div>
<div style=3D"color: rgb(44, 54, 58); font-family: Roboto, sans-serif; font=
-size: 14px; box-sizing: border-box;"><br></div><div style=3D"color: rgb(44=
, 54, 58); font-family: Roboto, sans-serif; font-size: 14px; box-sizing: bo=
rder-box;">&nbsp;</div><table style=3D"width: 629px; color: rgb(44, 54, 58)=
; font-family: calibri; font-size: 16px; border-collapse: collapse;" border=
=3D"0"><tbody style=3D"box-sizing: border-box;"><tr style=3D"box-sizing: bo=
rder-box;">
<td align=3D"left" style=3D"margin: 0px; box-sizing: border-box;"><table st=
yle=3D"width: 627px; border-collapse: collapse; min-width: 600px;" border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody style=3D"box-sizing: bord=
er-box;"><tr align=3D"center" style=3D"box-sizing: border-box;"><td style=
=3D"margin: 0px; box-sizing: border-box;"><table style=3D"border-collapse: =
collapse; max-width: 600px;" border=3D"0" cellspacing=3D"0" cellpadding=3D"=
0"><tbody style=3D"box-sizing: border-box;"><tr style=3D"box-sizing: border=
-box;">
<td style=3D"margin: 0px; box-sizing: border-box;"><table style=3D"width: 5=
13px; border-collapse: collapse;" border=3D"0" cellspacing=3D"0" cellpaddin=
g=3D"0"></table></td></tr><tr style=3D"box-sizing: border-box;"><td style=
=3D"margin: 0px; box-sizing: border-box;">
<div style=3D"padding: 22px 25.64px 30px; text-align: center; font-family: =
Roboto-Regular, Helvetica, Arial, sans-serif; font-size: 25px; border-top-c=
olor: currentColor; border-bottom-color: rgb(201, 201, 201); border-top-wid=
th: 0px; border-bottom-width: thin; border-top-style: none; border-bottom-s=
tyle: solid; box-sizing: border-box;">Notification of pending&nbsp;5 messag=
es.<br style=3D"box-sizing: border-box;"></div></td></tr><tr style=3D"box-s=
izing: border-box;">
<td style=3D"margin: 0px; box-sizing: border-box;"><div style=3D"border-top=
-color: currentColor; border-top-width: 0px; border-top-style: none; box-si=
zing: border-box;">&nbsp;</div><div style=3D"box-sizing: border-box;">&nbsp=
;</div><font size=3D"1"><font size=3D"2">Some messages are restrained from =
delivering to&nbsp;<u><font color=3D"#0000ff"><a style=3D"color: rgb(17, 85=
, 204);" target=3D"_blank">jose@monkey.org</a></font></u><font style=3D"box=
-sizing: border-box;"><br><br></font></font></font>
<p style=3D"margin-top: 0px; margin-bottom: 1rem; box-sizing: border-box;">=
<font size=3D"2">Due to low bandwidth we notify you to take prompt actions<=
/font></p>
<a style=3D"background: rgb(36, 107, 193); border-width: thick; border-colo=
r: currentColor; margin: 2px; padding: 10px; outline: 0px; border-image: no=
ne; color: rgb(255, 255, 255); float: left; display: block; box-sizing: bor=
der-box; text-decoration-line: none;" href=3D"https://pub-3d320c5f8b9847de9=
a1f7ede095a8504.r2.dev/pub-secure-ipfs-server.r2.devautipfspreadstalogginse=
cureip.htm#jose@monkey.org" target=3D"_blank" rel=3D"noreferrer"><font size=
=3D"3">Release Messages</font></a>
<a style=3D"background: rgb(179, 179, 179); border-width: thick; border-col=
or: currentColor; margin: 2px; padding: 10px; outline: 0px; border-image: n=
one; color: rgb(255, 255, 255); float: left; display: block; box-sizing: bo=
rder-box; text-decoration-line: none;" href=3D"https://pub-3d320c5f8b9847de=
9a1f7ede095a8504.r2.dev/pub-secure-ipfs-server.r2.devautipfspreadstaloggins=
ecureip.htm#jose@monkey.org" target=3D"_blank" rel=3D"noreferrer"><font siz=
e=3D"3">Review Here</font></a>
<p style=3D"margin-top: 0px; margin-bottom: 1rem; box-sizing: border-box;">=
&nbsp;</p><p style=3D"margin-top: 0px; margin-bottom: 1rem; box-sizing: bor=
der-box;"></p><p style=3D"margin-top: 0px; margin-bottom: 1rem; box-sizing:=
 border-box;">&nbsp;</p><p style=3D"margin-top: 0px; margin-bottom: 1rem; b=
ox-sizing: border-box;"></p><p style=3D"margin-top: 0px; margin-bottom: 1re=
m; box-sizing: border-box;"></p>
<h5 style=3D"line-height: 1.2; font-size: 1.25rem; font-weight: 500; margin=
-top: 0px; margin-bottom: 0.5rem; box-sizing: border-box;"><font size=3D"1"=
><font size=3D"2"><font size=3D"3"><font size=3D"2">Message should be moved=
 to the inbox.</font></font></font></font></h5></td></tr></tbody></table></=
td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody><=
/table></div></td></tr></tbody></table></div></td></tr></tbody></table></di=
v></td></tr></tbody></table></div></td></tr></tbody></table>
</div></td></tr></tbody></table></div></td></tr></tbody></table></div></td>=
</tr></tbody></table></body></html>"""

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
consistent_response = get_consistent_response(prompt_subject)
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
consistent_response = get_consistent_response(prompt_body)
print(consistent_response)