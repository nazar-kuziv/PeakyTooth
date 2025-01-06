from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
import sys

from controller.dentist_menu_controller import DentistMenuController

class DentistMenu(QMainWindow):
    def __init__(self, main_screen):
        super().__init__()
        self.controller = DentistMenuController(self)
        self.main_screen = main_screen
        self.setWindowTitle("Dentist Menu")
        self.setFixedSize(800, 850)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #FFFFFF;")

        # Definicje stylów dla poszczególnych przycisków
        add_patient_style = """
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4CAF50; /* Zielony przy hover */
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """

        find_patient_style = """
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF9800; /* Pomarańczowy przy hover */
            }
            QPushButton:pressed {
                background-color: #F57C00;
            }
        """

        create_appointment_style = """
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2196F3; /* Niebieski przy hover */
            }
            QPushButton:pressed {
                background-color: #1976D2;
            }
        """

        delete_appointment_style = """
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #F44336; /* Czerwony przy hover */
            }
            QPushButton:pressed {
                background-color: #D32F2F;
            }
        """

        # Tworzenie przycisków z indywidualnymi stylami
        self.add_patient_button = QPushButton("Add New Patient")
        self.add_patient_button.setFixedSize(165, 265)
        self.add_patient_button.setStyleSheet(add_patient_style)
        self.add_patient_button.clicked.connect(self.controller.patients_button_clicked)

        self.find_patient_button = QPushButton("Find Patient")
        self.find_patient_button.setFixedSize(165, 265)
        self.find_patient_button.setStyleSheet(find_patient_style)
        self.find_patient_button.clicked.connect(self.controller.patient_search_button_clicked)

        self.create_appointment_button = QPushButton("Create Appointment")
        self.create_appointment_button.setFixedSize(165, 265)
        self.create_appointment_button.setStyleSheet(create_appointment_style)
        self.create_appointment_button.clicked.connect(self.controller.create_appointment_button_clicked)

        self.delete_appointment_button = QPushButton("Delete Appointment")
        self.delete_appointment_button.setFixedSize(165, 265)
        self.delete_appointment_button.setStyleSheet(delete_appointment_style)
        self.delete_appointment_button.clicked.connect(self.controller.delete_appointment_button_clicked)

        # Dodawanie przycisków do layoutu
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = QWidget()
    dentist_menu = DentistMenu(main_screen)
    dentist_menu.show()
    sys.exit(app.exec())
