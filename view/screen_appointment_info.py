from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from controller.controller_appointment_info import ControllerAppointmentInfo


class ScreenAppointmentInfo(QWidget):
    def __init__(self, main_screen, appointment_id):
        super().__init__()
        self.main_screen = main_screen
        self.controller = ControllerAppointmentInfo(self, appointment_id)

        self.setWindowTitle("Appointment Information")
        self.setMinimumSize(600, 400)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        label_style = """
            QLabel {
                font-size: 16px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
        """

        self.label_appointment_id = QLabel()
        self.label_patient_name = QLabel()
        self.label_date = QLabel()
        self.label_time = QLabel()
        self.label_type = QLabel()
        self.label_notes = QLabel()

        labels = [
            self.label_appointment_id, self.label_patient_name,
            self.label_date, self.label_time, self.label_type, self.label_notes
        ]
        for label in labels:
            label.setStyleSheet(label_style)
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.main_layout.addWidget(label)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)

        # Different colors for each button
        edit_button_style = """
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
            QPushButton:pressed {
                background-color: #CD5B45;
            }
        """

        add_update_button_style = """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """

        view_pdf_button_style = """
            QPushButton {
                background-color: #1E90FF;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #1C86EE;
            }
            QPushButton:pressed {
                background-color: #1874CD;
            }
        """

        self.edit_button = QPushButton("Edit Appointment")
        self.edit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.edit_button.setStyleSheet(edit_button_style)
        self.edit_button.clicked.connect(self.controller.edit_appointment_button_clicked)
        self.button_layout.addWidget(self.edit_button)

        self.add_update_button = QPushButton("Add/Update Details")
        self.add_update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.add_update_button.setStyleSheet(add_update_button_style)
        self.add_update_button.clicked.connect(self.controller.add_details_button_clicked)
        self.button_layout.addWidget(self.add_update_button)

        self.view_pdf_button = QPushButton("PDF")
        self.view_pdf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.view_pdf_button.setStyleSheet(view_pdf_button_style)
        self.view_pdf_button.clicked.connect(self.controller.see_appointment_details_button_clicked)
        self.button_layout.addWidget(self.view_pdf_button)

        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
        self.controller.setAppointmentInfo()

    def refresh(self):
        self.controller.setAppointmentInfo()
