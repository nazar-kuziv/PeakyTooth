from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QDateEdit,
    QCheckBox,
    QWidget,
    QMessageBox,
    QSizePolicy
)
from PySide6.QtCore import Qt

from controller.new_patient_form_controller import NewPatientFormController


class NewPatientForm(QWidget):
    def __init__(self, main_screen):
        self.main_screen = main_screen
        super().__init__()
        self.setWindowTitle("New Patient Form")
        self.controller = NewPatientFormController(self)
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
            }
            QLabel {
                font-size: 16px;
            }
            QLineEdit, QComboBox, QDateEdit {
                border: 2px solid #C0C0C0;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
            QCheckBox {
                font-size: 16px;
            }
            QPushButton#submit_button {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton#submit_button:hover {
                background-color: #45A049;
            }
            QPushButton#submit_button:pressed {
                background-color: #3E8E41;
            }
        """)

        # Główny layout: QFormLayout
        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(50, 50, 50, 50)
        self.form_layout.setSpacing(20)

        self.setup_form()
        self.setLayout(self.form_layout)

    def setup_form(self):
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

        # Tworzymy przycisk Submit
        self.submit_button = QPushButton("Submit")
        self.submit_button.setObjectName("submit_button")
        # Aby rozciągnął się na całą szerokość:
        self.submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.submit_button.clicked.connect(self.controller.add_new_patient)

        # Dodajemy cały wiersz tylko z przyciskiem (span na całą szerokość)
        self.form_layout.addRow(self.submit_button)

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
