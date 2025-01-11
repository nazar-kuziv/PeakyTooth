from PySide6.QtWidgets import (
    QFormLayout, QLineEdit, QDateEdit, QTimeEdit, QComboBox, QTextEdit,
    QPushButton, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

from controller.controller_appointment_form import AppointmentFormController


class AppointmentForm(QWidget):
    def __init__(self, main_screen, patient_appointment_id, controller):
        super().__init__()

        self.main_screen = main_screen
        self.controller = controller(self, patient_appointment_id)

        self.setMinimumSize(400, 300)

        self.main_layout = QVBoxLayout()

        self.patient_info_layout = QHBoxLayout()

        self.patient_name_label = QLabel()

        self.patient_name_label.setStyleSheet("font-size: 14px;")

        self.name_surname_layout = QHBoxLayout()
        self.name_surname_layout.addWidget(self.patient_name_label)
        self.name_surname_layout.setSpacing(5)

        self.patient_info_layout.addLayout(self.name_surname_layout)

        # Add patient info to the main layout
        self.main_layout.addLayout(self.patient_info_layout)

        # Create form layout
        self.form_layout = QFormLayout()

        # Appointment Date
        self.date_field = QDateEdit()
        self.date_field.setCalendarPopup(True)  # Enables calendar picker
        self.date_field.setDisplayFormat("yyyy-MM-dd")
        self.form_layout.addRow("Date:", self.date_field)

        # Appointment Time
        self.time_field = QTimeEdit()
        self.time_field.setDisplayFormat("HH:mm")
        self.form_layout.addRow("Time:", self.time_field)

        # Doctor's Notes
        self.notes_field = QTextEdit()
        self.notes_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.form_layout.addRow("Notes:", self.notes_field)

        # Appointment Type
        self.type_field = QComboBox()
        self.type_field.addItems(["Consultation", "Procedure", "Follow-up", "Emergency"])
        self.form_layout.addRow("Type:", self.type_field)

        # Buttons
        self.create_button = QPushButton("Apply")
        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.addWidget(self.create_button)
        self.create_button.clicked.connect(self.controller.createAppointment)

        # Add form and buttons to the main layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

        self.controller.setAppointmentForm()

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)  # You can use Information, Warning, or Critical
        msg.setText(message)
        msg.exec()

