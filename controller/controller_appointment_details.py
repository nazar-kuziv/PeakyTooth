from utils.db_connection import DBConnection
from utils.user_session import UserSession


class ControllerAppointmentDetails:
    def __init__(self, view, appointment_id=None):
        self.view = view
        self.appointment_id = appointment_id
        self.current_appointment_details_data = None
        self.db = DBConnection()
        if self.appointment_id:
            self.current_appointment_details_data = self._get_current_appointment_details_data(self.appointment_id)

    def _get_current_appointment_details_data(self, appointment_id):
        try:
            appointment = self.db.get_appointment_details(UserSession().organization_id, appointment_id)
            if appointment:
                return appointment
            else:
                self.view.show_error("Cannot find the appointment.")
        except Exception as e:
            self.view.show_error(e)

    def get_services(self):
        try:
            return self.current_appointment_details_data[0]['services']
        except Exception:
            return None

    def get_symptoms_description(self):
        try:
            return self.current_appointment_details_data[0]['symptoms_description']
        except Exception:
            return None

    def get_mucous_membrane(self):
        try:
            return self.current_appointment_details_data[0]['mucous_membrane']
        except Exception:
            return None

    def get_periodontium(self):
        try:
            return self.current_appointment_details_data[0]['periodontium']
        except Exception:
            return None

    def get_hygiene(self):
        try:
            return self.current_appointment_details_data[0]['hygiene']
        except Exception:
            return None

    def get_oral_additional_info(self):
        try:
            return self.current_appointment_details_data[0]['oral_additional_info']
        except Exception:
            return None

    def get_dental_diagram(self):
        try:
            return self.current_appointment_details_data[0]['dental_diagram']
        except Exception:
            return None

    def get_additional_info(self):
        try:
            return self.current_appointment_details_data[0]['additional_info']
        except Exception:
            return None

    def get_medications(self):
        try:
            return self.current_appointment_details_data[0]['medications']
        except Exception:
            return None

    def get_date(self):
        try:
            return self.current_appointment_details_data[0]['date']
        except Exception:
            return None

    def get_time(self):
        try:
            return self.current_appointment_details_data[0]['time']
        except Exception:
            return None

    def get_patient_id(self):
        try:
            return self.current_appointment_details_data[0]['patient_id']
        except Exception:
            return None

    def get_dentist_id(self):
        try:
            return self.current_appointment_details_data[0]['dentist_id']
        except Exception:
            return None

    def get_organization_id(self):
        try:
            return self.current_appointment_details_data[0]['organization_id']
        except Exception:
            return None

    def get_type(self):
        try:
            return self.current_appointment_details_data[0]['type']
        except Exception:
            return None
