#D8VXQm4FGec2Hwe
#peakytooth@gmail.com
#lxvt lkcb vcap ewrz

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_pdf( patient_email, pdf_path):
    try:
        organizational_email = "peakytooth@gmail.com"
        app_password  = "lxvtlkcbvcapewrz"
        subject = "Your PDF Confirmation"
        body = "Dear Patient, please find the attached PDF document."




        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(organizational_email, app_password)


        msg = MIMEMultipart()
        msg['From'] = organizational_email
        msg['To'] = patient_email
        msg['Subject'] = subject


        msg.attach(MIMEText(body, 'plain'))


        with open(pdf_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {pdf_path}')

            msg.attach(part)

        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")



#send_email_with_pdf("vladyslav.meroniuk@gmail.com","BoardingCard_388552773_LPL_WAW.pdf" )



