from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QCheckBox,
    QPushButton,
    QMessageBox,
    QSizePolicy,
)

from controller.controller_new_patient import ControllerNewPatient


class ScreenNewPatient(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.setWindowTitle("New Patient Form")
        self.controller = ControllerNewPatient(self)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.form_layout = QFormLayout()
        self.setForm()

    def setForm(self):
        # Name Field
        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter patient's name")
        self.name_field.setFixedHeight(40)
        self.name_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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

        # Surname Field
        self.surname_field = QLineEdit()
        self.surname_field.setPlaceholderText("Enter patient's surname")
        self.surname_field.setFixedHeight(40)
        self.surname_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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

        # Sex Field
        self.sex_field = QComboBox()
        self.sex_field.addItems(["Male", "Female", "Other", "Prefer not to say"])
        self.sex_field.setFixedHeight(40)
        self.sex_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.sex_field.setStyleSheet("""
            QComboBox {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 5px 10px;
                font-size: 16px;
            }
            QComboBox:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Sex:", self.sex_field)

        # Date of Birth Field
        self.dob_field = QDateEdit()
        self.dob_field.setDisplayFormat("yyyy-MM-dd")
        self.dob_field.setCalendarPopup(True)
        self.dob_field.setFixedHeight(40)
        self.dob_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.dob_field.setStyleSheet("""
            QDateEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 5px 10px;
                font-size: 16px;
            }
            QDateEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Date of Birth:", self.dob_field)

        # Email Field
        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Enter email address")
        self.email_field.setFixedHeight(40)
        self.email_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.email_field.setStyleSheet("""
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
        self.form_layout.addRow("Email:", self.email_field)

        # Telephone Field
        self.telephone_field = QLineEdit()
        self.telephone_field.setPlaceholderText("Enter telephone number")
        self.telephone_field.setFixedHeight(40)
        self.telephone_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.telephone_field.setStyleSheet("""
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
        self.form_layout.addRow("Telephone:", self.telephone_field)

        # Allergy Checkbox
        self.allergy_checkbox = QCheckBox("Yes")
        self.allergy_checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 16px;
            }
        """)
        self.form_layout.addRow("Allergic to Analgesics?", self.allergy_checkbox)

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedHeight(50)
        self.submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #1F618D;
            }
            QPushButton:pressed {
                background-color: #154360;
            }
        """)
        self.submit_button.clicked.connect(self.controller.add_new_patient)
        self.form_layout.addRow(self.submit_button)

        # Add layout to main layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.submit_button)
        self.main_layout.addStretch()

    def show_message(self, message):
        if not message:
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('PeakyTooth - Message')
        msg.setText(message)
        msg.exec()
