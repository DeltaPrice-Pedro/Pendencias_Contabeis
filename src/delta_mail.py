from pathlib import Path
from os import  getenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / 'env' / '.env')

class DeltaMail:
    def __init__(self, companie: str, recipients: list[str], content: str):
        self.sender = getenv('SENDER_EMAIL')
        self.server = getenv("SMTP_SERVER","")
        self.port = getenv("SMTP_PORT", 0)
        
        self.smtp_username = getenv("EMAIL_SENDER","")
        self.smtp_password = getenv("PASSWRD_SENDER","")

        self.recipients = recipients

        self.msg = MIMEMultipart('mixed')
        self.msg['Subject'] = f'{companie} - PENDÊNCIAS CONTÁBEIS'
        self.msg['From'] =  self.sender
        self.msg['To'] = ', '.join(self.recipients)

        # self.recipients.append(self.sender)
        self.msg.attach(MIMEText(content, 'html', 'utf-8'))
        
    def attach(self, assign_filename: Path):
        with open(assign_filename, 'rb') as fp:
            image_data = fp.read()

        msg_image = MIMEImage(image_data)
        msg_image.add_header('Content-ID', f'<{assign_filename.stem}>')
        self.msg.attach(msg_image)

    def send(self):
        with smtplib.SMTP(self.server, self.port) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()

            smtp_server.login(self.smtp_username, self.smtp_password)
            smtp_server.sendmail(self.sender, self.recipients, self.msg.as_string())