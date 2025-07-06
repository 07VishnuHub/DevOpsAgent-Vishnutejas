import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, message):
    from_email = os.getenv("SMTP_USER")
    to_email = os.getenv("ALERT_EMAIL")

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, os.getenv("SMTP_PASS"))
            server.send_message(msg)
        return "Email sent."
    except Exception as e:
        return f"Email error: {e}"
