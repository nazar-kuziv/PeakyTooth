from PySide6.QtCore import QRegularExpression, QEvent
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QPushButton, \
    QMainWindow

from controller.controller_admin_menu import ControllerAdminMenu


class ScreenAdminMenu(QMainWindow):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = ControllerAdminMenu(self)
        self.setWindowTitle("Admin Menu")
        self.resize(800, 850)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #FFFFFF;")

        self.doctors_button = QPushButton("Doctors")
        self.doctors_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.doctors_button.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 28px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #FF8C00;  /* Orange hover effect */
            }
            QPushButton:pressed {
                background-color: #E67E22;
            }
        """)
        self.doctors_button.clicked.connect(self.controller.doctor_page_click)

        self.patients_button = QPushButton("Patients")
        self.patients_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.patients_button.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 28px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #2ECC71;  /* Green hover effect */
            }
            QPushButton:pressed {
                background-color: #27AE60;
            }
        """)
        self.patients_button.clicked.connect(self.controller.patients_button_click)

        button_layout.addStretch()
        button_layout.addWidget(self.doctors_button)
        button_layout.addSpacing(40)
        button_layout.addWidget(self.patients_button)
        button_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)

        self.setMouseTracking(True)
        self.doctors_button.setMouseTracking(True)
        self.patients_button.setMouseTracking(True)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            if source in (self.doctors_button, self.patients_button):
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #A9A9A9;
                        color: white;
                        border-radius: 15px;
                        font-size: 28px;
                        font-weight: bold;
                    }
                """)
        elif event.type() == QEvent.Leave:
            if source in (self.doctors_button, self.patients_button):
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #C0C0C0;
                        color: white;
                        border: none;
                        border-radius: 15px;
                        font-size: 28px;
                        font-weight: bold;
                    }
                """)
        return super().eventFilter(source, event)
