import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv, dotenv_values

from utils.environment import Environment
from utils.exceptions.smtp_unable_to_connect import SMTPUnableToConnect
from utils.exceptions.smtp_unable_to_send import SMTPUnableToSend

load_dotenv()


class SMTPConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SMTPConnection(metaclass=SMTPConnectionMeta):
    def __init__(self):
        env_vars = dotenv_values(Environment.resource_path(".env"))
        self.organizational_email = "peakytooth@gmail.com"
        app_password = env_vars.get("EMAIL_APP_PASSWORD")
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login(self.organizational_email, app_password)
        except:
            print('An error with SMTPConnection initialization')
            raise SMTPUnableToConnect()

    def sent_email_with_file(self, reciever_mail: str, subject: str, body: str, file_path: str):
        try:
            msg = MIMEMultipart()

            msg['From'] = self.organizational_email
            msg['To'] = reciever_mail
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {file_path}')

                msg.attach(part)

            self.server.send_message(msg)
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            raise SMTPUnableToSend()
