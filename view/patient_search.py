from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QApplication, QWidget, QFormLayout, QSizePolicy
)
from PySide6.QtCore import Qt
import sys

from controller.patient_search_controller import PatientSearchController


class PatientSearchForm(QWidget):
    def __init__(self, main_screen, controller):
        super().__init__()
        self.main_screen = main_screen

        self.setWindowTitle("Patient Search")
        self.controller = controller(self)

        # Set up the form layout
        self.form_layout = QFormLayout()

        # Search fields for patient ID, name, and surname
        self.id_field = QLineEdit()
        self.form_layout.addRow("Patient ID", self.id_field)

        self.name_field = QLineEdit()
        self.form_layout.addRow("Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Surname:", self.surname_field)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.controller.search_patients)

        # Add the form layout and search button into the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.search_button)

        # Set up the table to display search results
        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Adjust columns as needed
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Date of Birth", "Telephone", ""])
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
