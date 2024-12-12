from PySide6.QtWidgets import (
    QFormLayout, QLineEdit, QDateEdit, QTimeEdit, QComboBox, QTextEdit,
    QPushButton, QVBoxLayout, QWidget, QSizePolicy
)
from PySide6.QtCore import Qt


class AppointmentForm(QWidget):
    def __init__(self, main_screen, patient_id):
        super().__init__()

        self.main_screen = main_screen

        self.setWindowTitle("Create Appointment")
        self.setMinimumSize(400, 300)

        # Create main layout
        self.main_layout = QVBoxLayout()

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
        self.create_button = QPushButton("Create Appointment")
        self.cancel_button = QPushButton("Cancel")
        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.addWidget(self.create_button)
        self.button_layout.addWidget(self.cancel_button)

        # Add form and buttons to the main layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
