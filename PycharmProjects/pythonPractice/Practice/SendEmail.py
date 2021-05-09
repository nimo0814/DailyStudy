import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='nimo'
email['to']='daiyali'
email['subject']='nimo_subject'
email.set_content("nimo content of email")
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
smtp.starttls()
smtp.login("email_id","password")
smtp.send_message(email)
print("email send")