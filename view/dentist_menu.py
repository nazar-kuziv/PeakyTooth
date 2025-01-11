from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QEvent
import sys

from controller.dentist_menu_controller import DentistMenuController
from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm


class DentistMenu(QMainWindow):
    def __init__(self, main_screen):
        super().__init__()
        self.controller = DentistMenuController(self)
        self.main_screen = main_screen
        self.setWindowTitle("Dentist Menu")

        # Start the window maximized
        self.showMaximized()

        # Central widget setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setStyleSheet("background-color: #D3D3D3;")

        # Buttons for Dentist Menu
        self.add_patient_button = QPushButton("Add New Patient")
        self.add_patient_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.add_patient_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)
        self.add_patient_button.clicked.connect(self.controller.patients_button_clicked)

        self.find_patient_button = QPushButton("Find Patient")
        self.find_patient_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.find_patient_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)
        self.find_patient_button.clicked.connect(self.controller.patient_search_button_clicked)

        self.appointments_button = QPushButton("Appointments")
        self.appointments_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.appointments_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)
        self.appointments_button.clicked.connect(self.controller.appointments_button_clicked)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.add_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.find_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.appointments_button)
        button_layout.addStretch()

        # Adding layouts and spacers to main layout
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)

        # Installing event filters for hover effect
        self.add_patient_button.installEventFilter(self)
        self.find_patient_button.installEventFilter(self)
        self.appointments_button.installEventFilter(self)

    def eventFilter(self, source, event):
        # Hover effect for buttons
        if event.type() == QEvent.Enter:
            if source in (
                self.add_patient_button, self.find_patient_button,
                self.appointments_button
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
                self.appointments_button
            ):
                source.setStyleSheet("""
                    background-color: #C0C0C0;
                    border-radius: 10px;
                    font-size: 16px;
                """)

        return super().eventFilter(source, event)
