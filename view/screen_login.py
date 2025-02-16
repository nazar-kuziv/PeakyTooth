from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QFont, Qt, QPixmap, QRegularExpressionValidator, QKeySequence, QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QMessageBox

from controller.controller_login import ControllerLogin
from utils.environment import Environment
from utils.user_session import UserSession
from view.screen_admin_menu import ScreenAdminMenu
from view.screen_dentist_menu import ScreenDentistMenu
from view.screen_main import ScreenMain
from view.widget.button_base import ButtonBase


class ScreenLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = ControllerLogin(self)

        self.setWindowTitle('Login')
        self.setFixedSize(550, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        self.label_font = QFont("Segoe UI", 17)
        self.error_font = QFont("Segoe UI", 10)

        self.set_logo()
        self.set_username_label()
        self.set_username_input()
        self.set_username_error()
        self.set_password_label()
        self.set_password_input()
        self.set_password_error()
        self.set_login_button()
        self.set_enter_for_login()

    def set_logo(self):
        logo_label = QLabel()
        logo = QPixmap(Environment.resource_path('static/images/peaky.png'))
        logo = logo.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo)
        self.layout.addWidget(logo_label, alignment=Qt.AlignHCenter | Qt.AlignTop)

    def set_username_label(self):
        username_label = QLabel('Username')
        username_label.setFont(self.label_font)
        username_label.setStyleSheet("color: #333333;")
        self.layout.addWidget(username_label, alignment=Qt.AlignLeft | Qt.AlignTop)

    def set_username_input(self):
        self.username = QLineEdit()
        self.username.setFixedSize(350, 50)
        self.username.setPlaceholderText("Enter your username")
        self.username.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                background-color: #F5F5F5;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
                background-color: #FFFFFF;
            }
        """)
        non_empty_validator = QRegularExpressionValidator(QRegularExpression(r"^(?!\s*$).+"), self.username)
        self.username.setValidator(non_empty_validator)
        self.layout.addWidget(self.username, alignment=Qt.AlignHCenter)

    def set_username_error(self):
        self.username_error = QLabel()
        self.username_error.setStyleSheet('color: red')
        self.username_error.setFont(self.error_font)
        self.username_error.setVisible(False)
        self.layout.addWidget(self.username_error, alignment=Qt.AlignHCenter)

    def set_password_label(self):
        password_label = QLabel('Password')
        password_label.setFont(self.label_font)
        password_label.setStyleSheet("color: #333333;")
        self.layout.addWidget(password_label, alignment=Qt.AlignLeft | Qt.AlignTop)

    def set_password_input(self):
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedSize(350, 50)
        self.password.setPlaceholderText("Enter your password")
        self.password.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                background-color: #F5F5F5;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
                background-color: #FFFFFF;
            }
        """)
        non_empty_validator = QRegularExpressionValidator(QRegularExpression(r"^(?!\s*$).+"), self.password)
        self.password.setValidator(non_empty_validator)
        self.layout.addWidget(self.password, alignment=Qt.AlignHCenter)

    def set_password_error(self):
        self.password_error = QLabel()
        self.password_error.setStyleSheet('color: red')
        self.password_error.setFont(self.error_font)
        self.password_error.setVisible(False)
        self.layout.addWidget(self.password_error, alignment=Qt.AlignHCenter)

    def set_login_button(self):
        login_button = ButtonBase('Login')
        login_button.setFixedSize(250, 60)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        login_button.setDefault(True)
        login_button.clicked.connect(self.login)
        self.layout.addWidget(login_button, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addSpacing(20)

    def set_enter_for_login(self):
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self.login)

    def validate_username(self):
        if not self.username.hasAcceptableInput():
            self.password_error.setText('')
            self.password_error.setVisible(False)
            self.username_error.setText('Username required')
            self.username_error.setVisible(True)
            return False
        else:
            self.username_error.setText('')
            self.username_error.setVisible(False)
            return True

    def validate_password(self):
        if not self.password.hasAcceptableInput():
            self.password_error.setText('Password required')
            self.password_error.setVisible(True)
            return False
        else:
            self.password_error.setText('')
            self.password_error.setVisible(False)
            return True

    def login(self):
        if not self.validate_username() or not self.validate_password():
            return
        if self.controller.login(self.username.text(), self.password.text()):
            self.show_main_screen()

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', str(message))

    def show_main_screen(self):
        self.main_screen = ScreenMain()
        user_session = UserSession()
        if user_session.get_user_data()['role'] == 'Dentist':
            self.main_screen.add_screen_to_stack(ScreenDentistMenu(self.main_screen))
        elif user_session.get_user_data()['role'] == 'Admin':
            self.main_screen.add_screen_to_stack(ScreenAdminMenu(self.main_screen))
        self.main_screen.show()
        self.close()
