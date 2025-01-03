from PySide6.QtWidgets import (
    QFormLayout, QLineEdit, QDateEdit, QTimeEdit, QComboBox, QTextEdit,
    QPushButton, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

from controller.controller_appointment_editor import AppointmentEditorController

class AppointmentEditorForm(QWidget):
    def __init__(self, main_screen, appointment_id):
        super().__init__()

        self.main_screen = main_screen
        self.controller = AppointmentEditorController(self, appointment_id)

        self.setWindowTitle("Edit Appointment")
        self.setMinimumSize(400, 300)

        # Create main layout
        self.main_layout = QVBoxLayout()

        # Create patient info layout
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
        self.date_field.setCalendarPopup(True)
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
        self.save_button = QPushButton("Save Changes")
        self.cancel_button = QPushButton("Cancel")

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)

        # Connect button signals to controller methods
        self.save_button.clicked.connect(self.save_changes)
        self.cancel_button.clicked.connect(self.close)

        # Add form and buttons to the main layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

        self.controller.load_appointment_details()



    def show_message(self, message, title="Information"):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()

    def show_error(self, message):
        self.show_message(message, title="Error")

    def save_changes(self):
        date = self.date_field.date().toString("yyyy-MM-dd")
        time = self.time_field.time().toString("HH:mm")
        notes = self.notes_field.toPlainText()
        appointment_type = self.type_field.currentText()

        response = self.controller.update_appointment(date, time, notes, appointment_type)
        if response:
            self.show_message("Appointment updated successfully.")
            self.close()

    def delete_appointment(self):
        confirmation = QMessageBox.question(
            self, "Confirm Delete", "Are you sure you want to delete this appointment?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            response = self.controller.delete_appointment()
            if response:
                self.show_message("Appointment deleted successfully.")
                self.close()
