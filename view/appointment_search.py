from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QApplication, QWidget, QFormLayout, QSizePolicy, QDateEdit, QTimeEdit, QCheckBox, QComboBox
)
from PySide6.QtCore import Qt, QDate, QTime
import sys

from controller.controller_appointment_search import AppointmentSearchController
from view.widget.date_picker import DatePicker


class AppointmentSearchForm(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = AppointmentSearchController(self)

        self.setWindowTitle("Appointment Search")

        self.form_layout = QFormLayout()

        self.name_field = QLineEdit()
        self.form_layout.addRow("Patient Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Patient Surname:", self.surname_field)

        self.date_time_from_field = DatePicker()
        self.form_layout.addRow("From:", self.date_time_from_field)

        self.date_time_to_field = DatePicker()
        self.form_layout.addRow("To:", self.date_time_to_field)

        self.type_field = QComboBox()
        self.type_field.addItems(["-", "Consultation", "Procedure", "Follow-up", "Emergency"])
        self.form_layout.addRow("Type of Visit:", self.type_field)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.controller.search_appointments)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.search_button)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Patient", "Date", "Time", "Type", ""])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add the table to the main layout
        self.main_layout.addWidget(self.table)

        # Set the stretch factor for the table to 1 so it fills the remaining space
        self.main_layout.setStretch(0, 0)  # Form layout won't stretch
        self.main_layout.setStretch(1, 0)  # Button layout won't stretch
        self.main_layout.setStretch(2, 1)  # Table will stretch to take remaining space

        self.setLayout(self.main_layout)

        # Set size policy to ensure the table expands with the window
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

