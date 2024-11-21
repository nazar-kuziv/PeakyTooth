from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QEvent
import sys

from view.new_patient_form import NewPatientForm


class DentistMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dentist Menu")
        self.setFixedSize(800, 600)  # Increased window size

        # Central widget setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #D3D3D3;")

        # Buttons for Dentist Menu
        self.add_patient_button = QPushButton("Add New Patient")
        self.add_patient_button.setFixedSize(175, 200)  # Increased size to fit full text
        self.add_patient_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)
        self.add_patient_button.clicked.connect(self.open_add_patient_form)

        self.find_patient_button = QPushButton("Find Patient")
        self.find_patient_button.setFixedSize(175, 200)  # Increased size to fit full text
        self.find_patient_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)

        self.create_appointment_button = QPushButton("Create Appointment")
        self.create_appointment_button.setFixedSize(175, 200)  # Increased size to fit full text
        self.create_appointment_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)

        self.delete_appointment_button = QPushButton("Delete Appointment")
        self.delete_appointment_button.setFixedSize(175, 200)  # Increased size to fit full text
        self.delete_appointment_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)

        # Adding buttons to layouts
        button_layout.addStretch()
        button_layout.addWidget(self.add_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.find_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.create_appointment_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.delete_appointment_button)
        button_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)

        # Installing event filters for hover effect
        self.add_patient_button.installEventFilter(self)
        self.find_patient_button.installEventFilter(self)
        self.create_appointment_button.installEventFilter(self)
        self.delete_appointment_button.installEventFilter(self)

    def eventFilter(self, source, event):
        # Hover effect for buttons
        if event.type() == QEvent.Enter:
            if source in (
                self.add_patient_button, self.find_patient_button,
                self.create_appointment_button, self.delete_appointment_button
            ):
                source.setStyleSheet("""
                    background-color: #A9A9A9;
                    border-radius: 10px;
                    font-size: 16px;
                    color: white;
                """)
        elif event.type() == QEvent.Leave:
            if source in (
                self.add_patient_button, self.find_patient_button,
                self.create_appointment_button, self.delete_appointment_button
            ):
                source.setStyleSheet("""
                    background-color: #C0C0C0;
                    border-radius: 10px;
                    font-size: 16px;
                """)

        return super().eventFilter(source, event)

    def open_add_patient_form(self):
         self.setCentralWidget(NewPatientForm())

