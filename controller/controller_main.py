from PySide6.QtWidgets import QApplication

from utils.user_session import UserSession


class ControllerMain:
    def __init__(self, view):
        self.view = view
        self.user_session = UserSession()

    @staticmethod
    def logout():
        user_session = UserSession()
        user_session.logout()
        QApplication.exit()

    def get_user_role(self):
        return self.user_session.role

    def get_user_name_and_surname(self):
        return f'{self.user_session.name} {self.user_session.surname}'

    def get_user_organization(self):
        return self.user_session.organization_name
