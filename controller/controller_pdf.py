import base64
import io

from datetime import datetime
from PIL import Image
from PyPDFForm import PdfWrapper

from utils.db_connection import DBConnection
from utils.environment import Environment
from utils.smtp_connection import SMTPConnection

DATE_OF_VISIT_FIELD_NAME = 'dhFormfield-5377928304'
CLINIC_NAME_FIELD_NAME = 'dhFormfield-5377978379'
MAIL_FIELD_NAME = 'dhFormfield-5377991808'
PHONE_FIELD_NAME = 'dhFormfield-5378002748'
PATIENT_NAME_AND_SURNAME_FIELD_NAME = 'dhFormfield-5378020642'
PATIENT_SEX_FIELD_NAME = 'dhFormfield-5378032782'
PATIENT_DATE_OF_BIRTH_FIELD_NAME = 'dhFormfield-5378039424'
VISIT_TITLE_FIELD_NAME = 'dhFormfield-5378067475'
DESCRIPTION_OF_SYMPTOMS_FIELD_NAME = 'dhFormfield-5378092980'
MUCOUS_MEMBRANE_FIELD_NAME = 'dhFormfield-5378114752'
PERIODONTIUM_FIELD_NAME = 'dhFormfield-5378118427'
HYGIENE_FIELD_NAME = 'dhFormfield-5378119603'
ORAL_ADITIONAL_INFO_FIELD_NAME = 'dhFormfield-5378122231'
SERVICE_FIELD_NAME = 'dhFormfield-5378126960'
EIN_FIELD_NAME = 'dhFormfield-5378128254'
TREATMENTS_FIELD_NAME = 'dhFormfield-5378144126'
MEDICATIONS_FIELD_NAME = 'dhFormfield-5378145447'
ADDITIONAL_INFO_FIELD_NAME = 'dhFormfield-5378165977'


class ControllerPdf:
    """
    Can raise exceptions during initialization
    """

    def __init__(self, view, appointment_id):
        self.view = view
        self.smtp_connection = None
        self.pdf_path = None
        self.db = DBConnection()
        try:
            # self.appointment_details = self.db.get_appointment_details(UserSession().organization_id, appointment_id)
            self.appointment_details = self.db.get_appointment_data_for_pdf(1, appointment_id)
        except Exception as e:
            raise e

    def get_pdf_path(self):
        if not self.pdf_path:
            self.pdf_path = self._generate_pdf()
        return self.pdf_path

    def _generate_pdf(self):
        temp = PdfWrapper(Environment.resource_path('static/pdf_forms/dental_card.pdf'))
        # Clear all fields
        for key in self.appointment_details[0]:
            if not key == 'dental_diagram' and isinstance(self.appointment_details[0][key], str):
                self.appointment_details[0][key] = self.appointment_details[0][key].replace('\r', '')
        temp.fill({
            DATE_OF_VISIT_FIELD_NAME: self.get_visit_date(),
            CLINIC_NAME_FIELD_NAME: self.appointment_details[0]['organization_name'],
            MAIL_FIELD_NAME: self.appointment_details[0]['email'],
            PHONE_FIELD_NAME: self.appointment_details[0]['phone_number'],
            PATIENT_NAME_AND_SURNAME_FIELD_NAME: self.get_patient_name_and_surname(),
            PATIENT_SEX_FIELD_NAME: self.appointment_details[0]['sex'],
            PATIENT_DATE_OF_BIRTH_FIELD_NAME: self.appointment_details[0]['date_of_birth'],
            VISIT_TITLE_FIELD_NAME: self.appointment_details[0]['type'],
            DESCRIPTION_OF_SYMPTOMS_FIELD_NAME: self.appointment_details[0]['symptoms_description'],
            MUCOUS_MEMBRANE_FIELD_NAME: self.appointment_details[0]['mucous_membrane'],
            PERIODONTIUM_FIELD_NAME: self.appointment_details[0]['periodontium'],
            HYGIENE_FIELD_NAME: self.appointment_details[0]['hygiene'],
            ORAL_ADITIONAL_INFO_FIELD_NAME: self.appointment_details[0]['oral_additional_info'],
            SERVICE_FIELD_NAME: self.appointment_details[0]['services'],
            EIN_FIELD_NAME: self.appointment_details[0]['ein'],
            TREATMENTS_FIELD_NAME: self.appointment_details[0]['treatments'],
            MEDICATIONS_FIELD_NAME: self.appointment_details[0]['medications'],
            ADDITIONAL_INFO_FIELD_NAME: self.appointment_details[0]['additional_info']
        })
        if self.appointment_details[0]['dental_diagram']:
            image = Image.open(io.BytesIO(base64.b64decode(self.appointment_details[0]['dental_diagram'])))

            temp_image_path = "temp_diagram.png"
            image.save(temp_image_path, format="PNG")

            temp.draw_image(
                image=temp_image_path,
                page_number=2,
                x=20,
                y=542,
                width=375,
                height=247.5
            )
        file_name = f'output_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")}.pdf'
        with open(file_name, "wb+") as output:
            output.write(temp.read())
        return file_name

    def get_visit_date(self):
        try:
            result = ''
            if self.appointment_details[0]['date']:
                result = result + self.appointment_details[0]['date']
            if self.appointment_details[0]['time']:
                result = result + ' ' + self.appointment_details[0]['time'][:-3]
            return result
        except Exception as e:
            print(f"An error occurred while retrieving the visit date: {str(e)}")
            return ''

    def get_patient_name_and_surname(self):
        try:
            result = ''
            if self.appointment_details[0]['patient_name']:
                result = result + self.appointment_details[0]['patient_name']
            if self.appointment_details[0]['patient_surname']:
                result = result + ' ' + self.appointment_details[0]['patient_surname']
            return result
        except Exception as e:
            print(f"An error occurred while retrieving the visit date: {str(e)}")
            return ''

    def send_pdf_to_patient(self):
        try:
            if not self.smtp_connection:
                self.smtp_connection = SMTPConnection()
            self.smtp_connection.sent_email_with_file('n.kuziv2005@gmail.com', "Your Dental Card",
                                                      "I hope this message finds you well!\nAttached to this email, you will find your dental card in PDF format. This card contains important information and can be handy for quick access to your dental details.",
                                                      self.get_pdf_path())
            self.view.show_success('Email sent successfully!')
        except Exception as e:
            self.view.show_error(str(e))
            print(f'Exception(send_pdf_to_patient): {e}')
            return
