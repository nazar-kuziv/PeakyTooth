from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from controller.controller_full_patient_info import PatientInfoController


class PatientInfoScreen(QWidget):
    def __init__(self, main_screen, patient_id):
        super().__init__()
        self.main_screen = main_screen
        self.controller = PatientInfoController(self, patient_id)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)

        # Patient info labels (make them selectable)
        self.label_patient_id = QLabel()
        self.label_patient_name = QLabel()
        self.label_patient_surname = QLabel()
        self.label_patient_dob = QLabel()
        self.label_patient_sex = QLabel()
        self.label_patient_email = QLabel()
        self.label_patient_phone = QLabel()
        self.label_patient_allergy = QLabel()

        label_style = """
            font-size: 15px; 
        """
        for label in [
            self.label_patient_id, self.label_patient_name, self.label_patient_surname,
            self.label_patient_dob, self.label_patient_sex, self.label_patient_email,
            self.label_patient_phone, self.label_patient_allergy
        ]:
            label.setStyleSheet(label_style)  # Apply style to increase font size
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Enable text selection
            label.setWordWrap(True)  # Optional: Wrap text if it overflows

        # Adding labels to the layout
        self.main_layout.addWidget(self.label_patient_id)
        self.main_layout.addWidget(self.label_patient_name)
        self.main_layout.addWidget(self.label_patient_surname)
        self.main_layout.addWidget(self.label_patient_dob)
        self.main_layout.addWidget(self.label_patient_sex)
        self.main_layout.addWidget(self.label_patient_email)
        self.main_layout.addWidget(self.label_patient_phone)
        self.main_layout.addWidget(self.label_patient_allergy)

        # Buttons for editing and adding an appointment
        self.button_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edit")
        self.appointment_button = QPushButton("Create Appointment")

        self.edit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.appointment_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.edit_button.clicked.connect(self.controller.edit_button_clicked)
        self.appointment_button.clicked.connect(self.controller.create_appointment_button_clicked)

        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.appointment_button)

        # Adding buttons layout to the main layout
        self.main_layout.addLayout(self.button_layout)

        # Set main layout
        self.setLayout(self.main_layout)
        self.controller.setPatientInfo()
