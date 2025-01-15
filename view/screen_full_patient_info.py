from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from controller.controller_full_patient_info import ControllerPatientInfo


class ScreenPatientInfo(QWidget):
    def __init__(self, main_screen, patient_id):
        super().__init__()
        self.main_screen = main_screen
        self.controller = ControllerPatientInfo(self, patient_id)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)

        self.label_patient_id = QLabel()
        self.label_patient_name = QLabel()
        self.label_patient_surname = QLabel()
        self.label_patient_dob = QLabel()
        self.label_patient_sex = QLabel()
        self.label_patient_email = QLabel()
        self.label_patient_phone = QLabel()
        self.label_patient_allergy = QLabel()

        label_style = """
            font-size: 16px;
            padding: 8px 0;
            color: #2E2E2E;
        """
        for label in [
            self.label_patient_id, self.label_patient_name, self.label_patient_surname,
            self.label_patient_dob, self.label_patient_sex, self.label_patient_email,
            self.label_patient_phone, self.label_patient_allergy
        ]:
            label.setStyleSheet(label_style)
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setWordWrap(True)

        self.main_layout.addWidget(self.label_patient_id)
        self.main_layout.addWidget(self.label_patient_name)
        self.main_layout.addWidget(self.label_patient_surname)
        self.main_layout.addWidget(self.label_patient_dob)
        self.main_layout.addWidget(self.label_patient_sex)
        self.main_layout.addWidget(self.label_patient_email)
        self.main_layout.addWidget(self.label_patient_phone)
        self.main_layout.addWidget(self.label_patient_allergy)

        self.button_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edit")
        self.appointment_button = QPushButton("Create Appointment")

        self.edit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.appointment_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004377;
            }
        """)

        self.appointment_button.setStyleSheet("""
            QPushButton {
                background-color: #28A745;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1E7E34;
            }
        """)

        self.edit_button.clicked.connect(self.controller.edit_button_clicked)
        self.appointment_button.clicked.connect(self.controller.create_appointment_button_clicked)

        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.appointment_button)

        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
        self.controller.setPatientInfo()

    def refresh(self):
        self.controller.setPatientInfo()
