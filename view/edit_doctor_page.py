from PySide6.QtWidgets import (
    QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import QTimer


class EditDoctorPage(QWidget):
    def __init__(self, main_screen, doctor_id):
        super().__init__()
        self.main_screen = main_screen
        self.doctor_id = doctor_id

        self.setWindowTitle("Edit Doctor Page")

        self.form_layout = QFormLayout()
        self.setForm()

    def setForm(self):
        self.name_label = QLabel("Name:")
        self.name_field = QLineEdit()
        self.form_layout.addRow(self.name_label, self.name_field)

        self.surname_label = QLabel("Surname:")
        self.surname_field = QLineEdit()
        self.form_layout.addRow(self.surname_label, self.surname_field)

        self.login_label = QLabel("Login:")
        self.login_field = QLineEdit()
        self.form_layout.addRow(self.login_label, self.login_field)

        self.pass_label = QLabel("Password:")
        self.pass_field = QLineEdit()
        self.pass_field.setEchoMode(QLineEdit.Password)
        self.form_layout.addRow(self.pass_label, self.pass_field)

        self.submit_button = QPushButton("Save")
        self.submit_button.clicked.connect(self.update_doctor_info)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button)
        self.setLayout(main_layout)

    def update_doctor_info(self):
        from controller.edit_doctor_controller import EditDoctorController
        self.controller = EditDoctorController(self)

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
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(message))
        msg.exec()
