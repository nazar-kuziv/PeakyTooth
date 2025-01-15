
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
)

from controller.contoller_add_doctor import ControllerAddDoctor


class ScreenAddDoctor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Doctor Form")
        self.controller = ControllerAddDoctor(self)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.form_layout = QFormLayout()

        self.setForm()

    def setForm(self):
        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter doctor's name")
        self.name_field.setFixedHeight(40)
        self.name_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.surname_field.setPlaceholderText("Enter doctor's surname")
        self.surname_field.setFixedHeight(40)
        self.surname_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Surname:", self.surname_field)

        self.login_field = QLineEdit()
        self.login_field.setPlaceholderText("Enter login")
        self.login_field.setFixedHeight(40)
        self.login_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Login:", self.login_field)

        self.pass_field = QLineEdit()
        self.pass_field.setPlaceholderText("Enter password")
        self.pass_field.setEchoMode(QLineEdit.Password)
        self.pass_field.setFixedHeight(40)
        self.pass_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Password:", self.pass_field)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedHeight(40)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #1F618D;
            }
            QPushButton:pressed {
                background-color: #154360;
            }
        """)
        self.submit_button.clicked.connect(self.addDoctor)
        self.form_layout.addRow(self.submit_button)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addStretch()

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()

    def addDoctor(self):
        self.controller.add_doctor(
            self.name_field.text(),
            self.surname_field.text(),
            self.pass_field.text(),
            self.login_field.text()
        )
