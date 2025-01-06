import re
import bcrypt
from PySide6.QtCore import QDate
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

    def add_new_patient(self):
        # Extract data from UI fields
        name = self.view.name_field.text()
        surname = self.view.surname_field.text()
        date_of_birth = self.view.dob_field.text()
        sex = self.view.sex_field.currentText()
        email = self.view.email_field.text()
        telephone = self.view.telephone_field.text()
        analgesics_allergy = self.view.allergy_checkbox.isChecked()

        # Validate inputs
        if not name or not surname:
            self.view.show_message('Name and surname fields should not be empty')
            return

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            self.view.show_message('Invalid Email Address')
            return

        phone_regex = r'^\+?[\d\s\(\)-]{7,15}$'
        if not re.match(phone_regex, telephone):
            self.view.show_message('Invalid Phone Number')
            return

        # Add patient to database
        user_session = UserSession()
        message = self.db.addNewPatient(
            name, surname, date_of_birth, sex, email, telephone, analgesics_allergy, user_session.organization_id
        )

        self.view.show_message(message)

        # Clear all fields after successful addition
        self.view.name_field.clear()
        self.view.surname_field.clear()
        self.view.dob_field.setDate(QDate(2001, 1, 1))
        self.view.sex_field.setCurrentIndex(0)
        self.view.email_field.clear()
        self.view.telephone_field.clear()
        self.view.allergy_checkbox.setChecked(False)
