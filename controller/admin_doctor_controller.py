

import secrets
import string
import bcrypt
from PySide6.QtWidgets import QMessageBox

from utils.db_connection import DBConnection
from view.admin_doctor_page import AdminDoctorPage

class DoctorController:
    def __init__(self, view):
        self.view = view
        self.db = DBConnection()

    def add_doctor_form(self):
        from view.add_doctor_page import AddDoctorPage
        self.view.main_screen.setCentralWidget(AddDoctorPage())
        self.view.deleteLater()

    def get_doctors(self):
        try:
            doctors = self.db.get_doctors()
            return doctors
        except Exception as e:
            self.view.show_error(f"Error fetching doctors: {str(e)}")
            return []

    def search_doctors(self):
        try:
            name = self.view.name_field.text()
            surname = self.view.surname_field.text()
            doctors = self.db.search_doctors(name, surname)
            self.view.populate_table(doctors)
        except Exception as e:
            self.view.show_error(f"Error searching doctors: {str(e)}")



    def update_doctor_password(self, doctor_id):
        try:
            #new_password = self.generate_random_password()
            #hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.db.update_doctor_password(doctor_id, "NULL")

        except Exception as e:
            self.view.show_error(f"Error updating password: {str(e)}")

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for i in range(length))

    def delete_doctor_by_id(self, doctor_id):
        try:
            response = self.db.delete_doctor_by_id(doctor_id)
            return response
        except Exception as e:
            self.view.show_error(f"Error deleting doctor: {str(e)}")

    def doctor_page_click(self):
        self.view.main_screen.setCentralWidget(AdminDoctorPage(self.view.main_screen))
        self.view.deleteLater()



    def show_message(self, message):
        QMessageBox.information(self, "Information", message)