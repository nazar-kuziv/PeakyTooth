import bcrypt

from utils.db_connection import DBConnection


class ControllerEditDoctor:
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
