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

        # Appointment info labels (make them selectable)
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
            label.setStyleSheet(label_style)  # Apply style to increase font size
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Enable text selection
            label.setWordWrap(True)  # Optional: Wrap text if it overflows

        # Adding labels to the layout
        self.main_layout.addWidget(self.label_appointment_id)
        self.main_layout.addWidget(self.label_patient_name)
        self.main_layout.addWidget(self.label_date)
        self.main_layout.addWidget(self.label_time)
        self.main_layout.addWidget(self.label_type)
        self.main_layout.addWidget(self.label_notes)

        # Buttons for editing and rescheduling the appointment
        self.button_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edit Appointment")
        self.edit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.edit_button.clicked.connect(self.controller.edit_appointment_button_clicked)
        self.button_layout.addWidget(self.edit_button)

        self.view_pdf_button = QPushButton("View PDF")
        self.view_pdf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.view_pdf_button.clicked.connect(self.controller.view_pdf_button_clicked)
        self.button_layout.addWidget(self.view_pdf_button)


        # Adding buttons layout to the main layout
        self.main_layout.addLayout(self.button_layout)

        # Set main layout
        self.setLayout(self.main_layout)
        self.controller.setAppointmentInfo()
