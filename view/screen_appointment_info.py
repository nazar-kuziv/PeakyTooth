from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from controller.controller_appointment_info import AppointmentInfoController


class AppointmentInfoScreen(QWidget):
    def __init__(self, main_screen, appointment_id):
        super().__init__()
        self.main_screen = main_screen
        self.controller = AppointmentInfoController(self, appointment_id)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)

        self.label_appointment_id = QLabel()
        self.label_patient_name = QLabel()
        self.label_date = QLabel()
        self.label_time = QLabel()
        self.label_type = QLabel()
        self.label_notes = QLabel()

        label_style = """
            font-size: 15px; 
        """
        for label in [
            self.label_appointment_id, self.label_patient_name,
            self.label_date, self.label_time, self.label_type, self.label_notes
        ]:
            label.setStyleSheet(label_style)
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setWordWrap(True)
        self.main_layout.addWidget(self.label_appointment_id)
        self.main_layout.addWidget(self.label_patient_name)
        self.main_layout.addWidget(self.label_date)
        self.main_layout.addWidget(self.label_time)
        self.main_layout.addWidget(self.label_type)
        self.main_layout.addWidget(self.label_notes)

        self.button_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edit Appointment")
        self.edit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.edit_button.clicked.connect(self.controller.edit_appointment_button_clicked)
        self.button_layout.addWidget(self.edit_button)

        self.add_update_button = QPushButton("Add/Update details")
        self.add_update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.add_update_button.clicked.connect(self.controller.add_details_button_clicked)
        self.button_layout.addWidget(self.add_update_button)


        self.view_pdf_button = QPushButton("PDF")
        self.view_pdf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.view_pdf_button.clicked.connect(self.controller.see_appointment_details_button_clicked)
        self.button_layout.addWidget(self.view_pdf_button)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
        self.controller.setAppointmentInfo()

    def refresh(self):
        self.controller.setAppointmentInfo()