import bcrypt

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.user_session import UserSession


class ControllerLogin:
    def __init__(self, view):
        self.view = view

        try:
            self.db = DBConnection()
        except DBUnableToConnect as e:
            self.view.show_error(e)

    def login(self, login, password):
        try:
            db_user = self.db.get_user(login).data
        except DBUnableToGetData as e:
            self.view.show_error(e)
            return False
        if len(db_user) == 0 or not db_user[0]['password'] or not self._verify_password(
                db_user[0]['password'], password):
            self.view.show_error("Incorrect login data")
            return False
        user_session = UserSession()
        user_session.set_user_data(db_user[0]['userid'], db_user[0]['login'], db_user[0]['name'], db_user[0]['surname'],
                                   db_user[0]['role'], db_user[0]['organization_id'],
                                   db_user[0]['organizations']['organization_name'])
        return True

    @staticmethod
    def _verify_password(password_hash: str, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
