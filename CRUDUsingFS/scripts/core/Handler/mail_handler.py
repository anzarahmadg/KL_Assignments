import smtplib
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schema.studdent_schema import Email
from constants.agg_constants import agg
from scripts.utilities.mongodb import Students

def aggression():
    mail = Students.aggregate(agg)
    a_list = list(mail)
    print(a_list)
    return a_list[0]["total"]

def send_email(email: Email):
    sender_email = "anzar1ga20cs400@gmail.com"
    sender_password = "dwprmauiegydvrcr"
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject
    body = aggression()
    body = str(body)

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
