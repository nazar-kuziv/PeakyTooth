import re
import bcrypt
from pyexpat.errors import messages

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.user_session import UserSession


class NewPatientFormController:
    def __init__(self, view):
        self.view = view

        try:
            self.db = DBConnection()
        except DBUnableToConnect as e:
            self.view.show_error(e)

    def add_new_patient(self, name, surname, date_of_birth, sex,  email, telephone, analgesics_allergy):
        if name == '' or surname == '':
            self.view.show_message('Name and surname fields should not be empty')
            return
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email) is None:
            self.view.show_message('Invalid Email Address')
            return
        phone_regex = r'^\+?[\d\s\(\)-]{7,15}$'
        if re.match(phone_regex, telephone) is None:
            self.view.show_message('Invalid Phone Number')
            return
        user_session = UserSession()
        message = self.db.addNewPatient(name, surname, date_of_birth, sex, email, telephone, analgesics_allergy, user_session.organization_id)
        self.view.show_message(message)
