from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QFont, Qt, QPixmap, QRegularExpressionValidator, QKeySequence, QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QMessageBox, QPushButton

from controller.controller_login import ControllerLogin
from utils.environment import Environment


class ScreenLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = ControllerLogin(self)

        self.setWindowTitle('Login')
        self.setFixedSize(500, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # noinspection PyUnresolvedReferences
        self.layout.setAlignment(Qt.AlignHCenter)

        self.label_font = QFont()
        self.label_font.setPointSize(17)

        self.error_font = QFont()
        self.error_font.setPointSize(10)

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
        logo = QPixmap(Environment.resource_path('static/images/icon.png'))
        logo = logo.scaled(150, 150)
        logo_label.setPixmap(logo)
        # noinspection PyUnresolvedReferences
        self.layout.addWidget(logo_label, alignment=Qt.AlignHCenter)

    def set_username_label(self):
        username_label = QLabel('Username')
        username_label.setFont(self.label_font)
        self.layout.addWidget(username_label)

    def set_username_input(self):
        self.username = QLineEdit()
        self.username.setFixedSize(300, 30)
        non_empty_validator = QRegularExpressionValidator(QRegularExpression(r"^(?!\s*$).+"), self.username)
        self.username.setValidator(non_empty_validator)
        self.layout.addWidget(self.username)

    def set_username_error(self):
        self.username_error = QLabel()
        self.username_error.setStyleSheet('color: red')
        self.username_error.setFont(self.error_font)
        self.username_error.setVisible(False)
        self.layout.addWidget(self.username_error)

    def set_password_input(self):
        self.password = QLineEdit()
        # noinspection PyUnresolvedReferences
        self.password.setEchoMode(QLineEdit.Password)

        self.password.setFixedSize(300, 30)
        non_empty_validator = QRegularExpressionValidator(QRegularExpression(r"^(?!\s*$).+"), self.password)
        self.password.setValidator(non_empty_validator)
        self.layout.addWidget(self.password)

    def set_password_error(self):
        self.password_error = QLabel()
        self.password_error.setStyleSheet('color: red')
        self.password_error.setFont(self.error_font)
        self.password_error.setVisible(False)
        self.layout.addWidget(self.password_error)

    def set_login_button(self):
        login_button = QPushButton('Login')
        login_button.setFixedSize(200, 60)
        login_button.setDefault(True)
        login_button.clicked.connect(self.login)
        # noinspection PyUnresolvedReferences
        self.layout.addWidget(login_button, alignment=Qt.AlignHCenter)

    def set_enter_for_login(self):
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self.login)

    def set_password_label(self):
        password_label = QLabel('Password')
        password_label.setFont(self.label_font)
        self.layout.addWidget(password_label)

    def validate_username(self):
        if not self.username.hasAcceptableInput():
            self.password_error.setText('')
            self.password_error.setVisible(False)
            self.username_error.setText('Uncorrect username')
            self.username_error.setVisible(True)
            return False
        else:
            self.username_error.setText('')
            self.username_error.setVisible(False)
            return True

    def validate_password(self):
        if not self.password.hasAcceptableInput():
            self.password_error.setText('Uncorrect password')
            self.password_error.setVisible(True)
            return False
        else:
            self.password_error.setText('')
            self.password_error.setVisible(False)
            return True

    def login(self):
        if not self.validate_username() or not self.validate_password():
            return
        self.controller.login(self.username.text(), self.password.text())

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

    def show_primary_screen(self):
        pass
        # self.primary_screen = ScreenPrimary()
        # self.primary_screen.show()
        # self.close()
