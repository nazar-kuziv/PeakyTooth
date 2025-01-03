from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QApplication, QWidget, QFormLayout, QSizePolicy, QDateEdit, QTimeEdit
)
from PySide6.QtCore import Qt, QDate, QTime
import sys

from controller.controller_appointment_search import AppointmentSearchController


class AppointmentSearchForm(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = AppointmentSearchController(self)

        self.setWindowTitle("Appointment Search")

        # Set up the form layout
        self.form_layout = QFormLayout()

        # Search fields for patient name and surname
        self.name_field = QLineEdit()
        self.form_layout.addRow("Patient Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Patient Surname:", self.surname_field)

        # Search fields for date range (from and to)
        self.date_from_field = QDateEdit()
        self.date_from_field.setCalendarPopup(True)
        self.date_from_field.setDate(QDate.currentDate())
        self.form_layout.addRow("Date From:", self.date_from_field)

        self.date_to_field = QDateEdit()
        self.date_to_field.setCalendarPopup(True)
        self.date_to_field.setDate(QDate.currentDate())
        self.form_layout.addRow("Date To:", self.date_to_field)

        # Search field for type of visit
        self.type_field = QLineEdit()
        self.form_layout.addRow("Type of Visit:", self.type_field)

        # Search fields for time range (from and to)
        self.time_from_field = QTimeEdit()
        self.time_from_field.setTime(QTime(0, 0))
        self.form_layout.addRow("Time From:", self.time_from_field)

        self.time_to_field = QTimeEdit()
        self.time_to_field.setTime(QTime(23, 59))
        self.form_layout.addRow("Time To:", self.time_to_field)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.controller.search_appointments)

        # Add the form layout and search button into the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.search_button)

        # Set up the table to display search results
        self.table = QTableWidget()
        self.table.setColumnCount(7)  # Adjust columns as needed
        self.table.setHorizontalHeaderLabels(["ID", "Patient Name", "Patient Surname", "Date", "Time", "Type", "Notes"])
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





app = QApplication(sys.argv)
main_screen = None
form = AppointmentSearchForm(main_screen)
form.show()
sys.exit(app.exec())
