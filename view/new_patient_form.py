from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QDateEdit,
    QCheckBox,
    QWidget,
    QMessageBox
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
            QPushButton#back_button {
                background-color: #2980B9;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton#back_button:hover {
                background-color: #1F618D;
            }
            QPushButton#back_button:pressed {
                background-color: #154360;
            }
            QFormLayout {
                spacing: 20px;
            }
        """)

        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(50, 50, 50, 50)
        self.form_layout.setSpacing(20)
        self.setForm()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addSpacing(30)
        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(self.back_button)
        main_layout.addStretch()
        self.setLayout(main_layout)

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
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.controller.add_new_patient)

        self.back_button = QPushButton("Back")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.go_back)

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
