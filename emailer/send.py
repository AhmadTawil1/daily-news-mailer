import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(subject: str, html_content: str, to_email: str = None) -> bool:
    if to_email is None:
        to_email = EMAIL_ADDRESS

    try:
        # 1. Build the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = EMAIL_ADDRESS
        message["To"] = to_email

        # Add HTML body
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)

        # 2. Connect to the SMTP server securely (TLS)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, message.as_string())

        print(f"✅ Email sent to {to_email}")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False
