from email.message import EmailMessage
from passwords import email_password 
import ssl
import smtplib

email_sender = 'adamwest023@gmail.com'
email_password = email_password
 
 
email_receiver = "hejan95984@lurenwu.com"

subject = "Don't forget to subscribe."
body = """
When you watch a video, please be sure to subscribe
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver,em.as_string())
        
 
