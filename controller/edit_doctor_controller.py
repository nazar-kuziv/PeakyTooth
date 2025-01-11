

import secrets
import string
import bcrypt
from PySide6.QtWidgets import QMessageBox

from utils.db_connection import DBConnection
from view.admin_doctor_page import AdminDoctorPage
from view.edit_doctor_page import EditDoctorPage


class EditDoctorController:
    def __init__(self, view):
        self.view = view
        self.db = DBConnection()



    def change_doctor_surname(self, doctor_id, new_surname):
        try:
            self.db.update_doctor_surname(doctor_id, new_surname)
        except Exception as e:
            self.view.show_error(f"Error updating surname: {str(e)}")







    def update_doctor_password(self, doctor_id, new_password):
        try:
            #new_password = self.generate_random_password()
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.db.update_doctor_password(doctor_id, hashed_password)

        except Exception as e:
            self.view.show_error(f"Error updating password: {str(e)}")



    def change_doctor_name(self, doctor_id, new_name):
        try:
            self.db.update_dotor_name(doctor_id, new_name)
        except Exception as e:
            self.view.show_error(f"Error updating name: {str(e)}")

    def change_doctor_login(self, doctor_id, new_login):
        try:
            self.db.update_doctor_login(doctor_id, new_login)
        except Exception as e:
            self.view.show_error(f"Error updating login: {str(e)}")





    def show_message(self, message):
        QMessageBox.information(self, "Information", message)