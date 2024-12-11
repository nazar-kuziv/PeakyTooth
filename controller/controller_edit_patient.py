import datetime
import re

from utils.db_connection import DBConnection
from utils.user_session import UserSession


class ControllerEditPatient:
    def __init__(self, view, patient_id):
        self.view = view
        self.patient_id = patient_id
        self.db = DBConnection()
        self.current_patient_data = self._get_current_pattient_data()

    def alter_patient_data(self, name, surname, date_of_birth, analegisics_allergy,
                           telephone, email):
        try:
            response = self.db.alter_patient_data(UserSession().organization_id, self.patient_id, name, surname,
                                                  date_of_birth,
                                                  analegisics_allergy, telephone, email)
            if response:
                return response
            else:
                self.view.show_error("Cannot find the patient.")
        except Exception as e:
            self.view.show_error(e)

    def get_patient_name(self):
        try:
            return self.current_patient_data[0]['patient_name']
        except Exception:
            return None

    def get_patient_surname(self):
        try:
            return self.current_patient_data[0]['patient_surname']
        except Exception:
            return None

    def get_patient_date_of_birth(self):
        try:
            return self.current_patient_data[0]['date_of_birth']
        except Exception:
            return None

    def get_patient_analgesics_allergy(self):
        try:
            return self.current_patient_data[0]['analgesics_allergy']
        except Exception:
            return None

    def get_patient_email(self):
        try:
            return self.current_patient_data[0]['email']
        except Exception:
            return None

    def get_patient_phone_number(self):
        try:
            return self.current_patient_data[0]['telephone']
        except Exception:
            return None

    @staticmethod
    def is_name_surname_valid(name: str):
        if name:
            name_regex = r"^[A-Za-z]+$"
            return bool(re.match(name_regex, name))
        return False

    @staticmethod
    def is_date_valid(date: str) -> bool:
        if date:
            date_regex = r"^\d{4}-\d{2}-\d{2}$"
            if re.match(date_regex, date):
                try:
                    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
                    if date_obj <= datetime.datetime.now() and date_obj.year >= 1900:
                        return True
                except ValueError:
                    return False
        return False

    @staticmethod
    def is_email_valid(email: str) -> bool:
        if email:
            email_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
            return bool(re.match(email_regex, email))
        return False

    @staticmethod
    def is_phone_number_valid(mobile: str) -> bool:
        if mobile:
            mobile_regex = r"^\+?[1-9]\d{1,14}$"
            return bool(re.match(mobile_regex, mobile))
        return False

    def _get_current_pattient_data(self):
        try:
            patient = self.db.get_patient(UserSession().organization_id, self.patient_id)
            if patient:
                return patient
            else:
                self.view.show_error("Cannot find the patient.")
        except Exception as e:
            self.view.show_error(e)
