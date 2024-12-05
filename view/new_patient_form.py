from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QDateEdit,
    QCheckBox,
    QApplication,
    QWidget, QMessageBox,
)
from PySide6.QtCore import Qt
import sys

from controller.new_patient_form_controller import NewPatientFormController


class NewPatientForm(QWidget):
    def __init__(self, main_screen):
        self.main_screen = main_screen
        super().__init__()
        self.setWindowTitle("New patient form")
        self.controller = NewPatientFormController(self)

        # Initialize the form layout
        self.form_layout = QFormLayout()

        # Add the input fields
        self.setForm()

    def setForm(self):
        self.name_field = QLineEdit()
        self.form_layout.addRow("Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Surname:", self.surname_field)

        self.sex_field = QComboBox()
        self.sex_field.addItems(["Male", "Female", "Other", "Prefer not to say"])
        self.form_layout.addRow("Sex:", self.sex_field)

        self.dob_field = QDateEdit()
        self.dob_field.setDisplayFormat("yyyy-MM-dd")
        self.dob_field.setCalendarPopup(True)
        self.form_layout.addRow("Date of Birth:", self.dob_field)

        self.email_field = QLineEdit()
        self.form_layout.addRow("Email:", self.email_field)

        self.telephone_field = QLineEdit()
        self.form_layout.addRow("Telephone:", self.telephone_field)

        self.allergy_checkbox = QCheckBox("Yes")
        self.form_layout.addRow("Allergic to Analgesics?", self.allergy_checkbox)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.controller.add_new_patient)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button)
        self.setLayout(main_layout)

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)  # You can use Information, Warning, or Critical
        msg.setText(message)
        msg.exec()



