import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "phanindranaidu222@gmail.com"  # Replace with your email
SENDER_PASSWORD = "yxpc vbeg gyhr bdhl"  # Replace with your email password
RECIPIENT_EMAIL = "phanindranaidug@gmail.com"  # Replace with the recipient's email

# Email Content
SUBJECT = "Test Email"
BODY = """\
Dear User,

This is a test email to verify the email-sending functionality.

Best regards,
Your Application
"""

try:
    # Create the email message
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = SUBJECT
    message.attach(MIMEText(BODY, "plain"))

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
        print(f"Email sent successfully to {RECIPIENT_EMAIL}")
except Exception as e:
    print(f"Error sending email: {e}")
