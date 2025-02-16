from PySide6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)

class ScreenEditDoctor(QWidget):
    def __init__(self, main_screen, doctor_id):
        super().__init__()
        self.main_screen = main_screen
        self.doctor_id = doctor_id

        self.setWindowTitle("Edit Doctor Page")

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
                padding: 4px;
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
                padding: 4px;
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
                padding: 4px;
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
                padding: 4px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Password:", self.pass_field)

        self.submit_button = QPushButton("Save")
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
                background-color: #1F618D; /* Darker blue */
            }
            QPushButton:pressed {
                background-color: #154360;
            }
            QPushButton:disabled {
                background-color: #A9A9A9;
                color: white;
            }
        """)
        self.submit_button.clicked.connect(self.update_doctor_info)
        self.form_layout.addRow(self.submit_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

    def update_doctor_info(self):
        from controller.controller_edit_doctor import ControllerEditDoctor
        self.controller = ControllerEditDoctor(self)

        if self.name_field.text():
            self.controller.change_doctor_name(self.doctor_id, self.name_field.text())
        if self.surname_field.text():
            self.controller.change_doctor_surname(self.doctor_id, self.surname_field.text())
        if self.login_field.text():
            self.controller.change_doctor_login(self.doctor_id, self.login_field.text())
        if self.pass_field.text():
            self.controller.update_doctor_password(self.doctor_id, self.pass_field.text())

        self.show_message("Changes saved")

    def show_message(self, message):
        if not message:
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('PeakyTooth - Message')
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(message))
        msg.exec()
