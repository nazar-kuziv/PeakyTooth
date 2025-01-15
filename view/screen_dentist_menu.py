
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)

from controller.controller_dentist_menu import ControllerDentistMenu


class ScreenDentistMenu(QMainWindow):
    def __init__(self, main_screen):
        super().__init__()
        self.controller = ControllerDentistMenu(self)
        self.main_screen = main_screen
        self.setWindowTitle("Dentist Menu")

        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        central_widget.setStyleSheet("background-color: #FFFFFF;")

        button_style = """
            QPushButton {
                background-color: #C0C0C0;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 20px;
                font-weight: bold;
                padding: 15px 30px;
            }
        """

        self.add_patient_button = QPushButton("Add New Patient")
        self.add_patient_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.add_patient_button.setStyleSheet(button_style)
        self.add_patient_button.clicked.connect(self.controller.patients_button_clicked)

        self.find_patient_button = QPushButton("Find Patient")
        self.find_patient_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.find_patient_button.setStyleSheet(button_style)
        self.find_patient_button.clicked.connect(self.controller.patient_search_button_clicked)

        self.appointments_button = QPushButton("Appointments")
        self.appointments_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.appointments_button.setStyleSheet(button_style)
        self.appointments_button.clicked.connect(self.controller.appointments_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.add_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.find_patient_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.appointments_button)
        button_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.add_patient_button.installEventFilter(self)
        self.find_patient_button.installEventFilter(self)
        self.appointments_button.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            if source == self.add_patient_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #27AE60;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
            elif source == self.find_patient_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #2980B9;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
            elif source == self.appointments_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #8E44AD;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
        elif event.type() == QEvent.Leave:
            if source == self.add_patient_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #C0C0C0;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
            elif source == self.find_patient_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #C0C0C0;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
            elif source == self.appointments_button:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #C0C0C0;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 15px 30px;
                    }
                """)
        return super().eventFilter(source, event)
