import re
import bcrypt
from pyexpat.errors import messages

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.user_session import UserSession

class DeleteDentistController:
        def __init__(self, view):
            self.view = view

            try:
                self.db = DBConnection()
            except DBUnableToConnect as e:
                self.view.show_error(e)


        def delete_dentist(self, dentist_id):
            try:
                dentist_id.strip()
            except:
                pass

            if dentist_id == '':
                self.view.show_message('  ID shouldnt be empty')
                return

            try:
                message = self.db.delete_dentist(dentist_id)
                self.view.show_message(message)
            except Exception as e:
                self.view.show_error(f"error: {str(e)}")
