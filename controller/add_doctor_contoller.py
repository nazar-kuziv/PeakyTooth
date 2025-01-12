import bcrypt

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.user_session import UserSession


class AddDoctorController:
    def __init__(self, view):
        self.view = view

        try:
            self.db = DBConnection()
        except DBUnableToConnect as e:
            self.view.show_error(e)

    def add_doctor(self, name, surname, password, login):

        try:
            password.strip()
        except:
            pass

        if name == '' or surname == '':
            self.view.show_message('Name and surname fields should not be empty')
            return

        if len(password) < 8:
            self.view.show_message('Password should be at least 8 characters long')
            return

        try:
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        except Exception as e:
            self.view.show_error(f"Error hashing password: {str(e)}")
            return

        user_session = UserSession()
        organization_id = user_session.organization_id

        try:
            message = self.db.addNewDoctor(name, surname, login, password_hash, organization_id)
            self.view.show_message(message)
        except Exception as e:
            self.view.show_error(f"Error add doctor: {str(e)}")
