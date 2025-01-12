from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QEvent
import sys

from controller.admin_menu_controller import AdminMenuController


class AdminMenu(QMainWindow):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = AdminMenuController(self)
        self.setWindowTitle("Admin Menu")
        self.setFixedSize(800, 850)  # Increased window size for better layout

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #FFFFFF;")  # Modern background color

        # Styled Doctors Button
        self.doctors_button = QPushButton("Doctors")
        self.doctors_button.setFixedSize(250, 400)
        self.doctors_button.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 28px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1F618D;
            }
        """)
        self.doctors_button.clicked.connect(self.controller.doctors_button_click)

        # Styled Patients Button
        self.patients_button = QPushButton("Patients")
        self.patients_button.setFixedSize(250, 400)
        self.patients_button.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 28px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D35400;
            }
            QPushButton:pressed {
                background-color: #BA4A00;
            }
        """)

        button_layout.addStretch()
        button_layout.addWidget(self.doctors_button)
        button_layout.addSpacing(40)  # Increased spacing between buttons
        button_layout.addWidget(self.patients_button)
        button_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)

        self.patients_button.clicked.connect(self.controller.patients_button_click)


    def eventFilter(self, source, event):
        return super().eventFilter(source, event)
