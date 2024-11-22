import re
import bcrypt
from pyexpat.errors import messages

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

        def add_doctor(self, name, surname, password):
            if name == '' or surname == '':
                self.view.show_message('Name and surname fields should not be empty')
                return

            if len(password) < 8 :
                self.view.show_message('Password should be at least 8 characters long')
                return


            user_session = UserSession()
            message = self.db.addNewDoctor(name, surname,password, user_session.organization_id)
            self.view.show_message(message)