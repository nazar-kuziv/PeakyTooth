from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QDateEdit,
    QCheckBox,
    QWidget, QMessageBox
)
from PySide6.QtCore import Qt

from controller.new_patient_form_controller import NewPatientFormController


class NewPatientForm(QWidget):
    def __init__(self, main_screen):
        self.main_screen = main_screen
        super().__init__()
        self.setWindowTitle("New patient form")
        self.controller = NewPatientFormController(self)

        # Initialize the form layout
        self.form_layout = QFormLayout()
        self.setForm()

    def setForm(self):
        # Pola formularza
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

        # BACK button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        # Layout główny
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(self.back_button)  # <--- przycisk Back

        self.setLayout(main_layout)

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()

    def go_back(self):

        from utils.user_session import UserSession
        role = UserSession().role

        if role == "Admin":
            from view.admin_menu import AdminMenu
            self.main_screen.setCentralWidget(AdminMenu(self.main_screen))
        else:
            from view.dentist_menu import DentistMenu
            self.main_screen.setCentralWidget(DentistMenu(self.main_screen))

        self.deleteLater()
