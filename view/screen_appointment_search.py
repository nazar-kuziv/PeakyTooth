from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QComboBox,
    QSizePolicy,
    QHeaderView,
    QMessageBox
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QFont

from controller.controller_appointment_search import ControllerAppointmentSearch
from view.widget.date_picker import DatePicker

class ScreenAppointmentSearch(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = ControllerAppointmentSearch(self)

        self.setWindowTitle("Appointment Search")
        self.setMinimumSize(800, 600)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.form_layout = QFormLayout()
        self.setForm()

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addSpacing(20)

        self.search_button = QPushButton("Search")
        self.search_button.setFixedHeight(50)
        self.search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #C0C0C0;
            }
            QPushButton:pressed {
                background-color: #154360;
            }
        """)
        self.search_button.clicked.connect(self.controller.search_appointments)
        self.main_layout.addWidget(self.search_button)

        self.main_layout.addSpacing(20)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Patient", "Date", "Time", "Type", "Actions"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #CCCCCC;
                gridline-color: #E0E0E0;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #F0F0F0;
                padding: 4px;
                border: 1px solid #CCCCCC;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.main_layout.addWidget(self.table)

        self.search_button.installEventFilter(self)

    def setForm(self):
        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter patient's name")
        self.name_field.setFixedHeight(40)
        self.name_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.name_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 4px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Patient Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.surname_field.setPlaceholderText("Enter patient's surname")
        self.surname_field.setFixedHeight(40)
        self.surname_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.surname_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 4px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Patient Surname:", self.surname_field)

        self.date_time_from_field = DatePicker()
        self.date_time_from_field.setFixedHeight(50)
        self.date_time_from_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.date_time_from_field.setStyleSheet("""
            QDateTimeEdit {
                background-color: #ffffff;
                border: 1px solid #c2c2c2;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
                color: #333333;
            }
            QDateTimeEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #c2c2c2;
                background-color: #ededed;
            }
            QDateTimeEdit:hover {
                background-color: #f7f7f7;
            }
            QDateTimeEdit:focus {
                border: 1px solid #66AFE9;
                background-color: #ffffff;
            }
        """)
        self.form_layout.addRow("From:", self.date_time_from_field)

        self.date_time_to_field = DatePicker()
        self.date_time_to_field.setFixedHeight(50)
        self.date_time_to_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.date_time_to_field.setStyleSheet("""
            QDateTimeEdit {
                background-color: #ffffff;
                border: 1px solid #c2c2c2;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
                color: #333333;
            }
            QDateTimeEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #c2c2c2;
                background-color: #ededed;
            }
            QDateTimeEdit:hover {
                background-color: #f7f7f7;
            }
            QDateTimeEdit:focus {
                border: 1px solid #66AFE9;
                background-color: #ffffff;
            }
        """)
        self.form_layout.addRow("To:", self.date_time_to_field)

        self.type_field = QComboBox()
        self.type_field.addItems(["-", "Consultation", "Procedure", "Follow-up", "Emergency"])
        self.type_field.setFixedHeight(40)
        self.type_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.type_field.setStyleSheet("""
            QComboBox {
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 4px;
                font-size: 16px;
                background-color: #ffffff;
            }
            QComboBox:focus {
                border: 2px solid #66AFE9;
            }
        """)
        self.form_layout.addRow("Type of Visit:", self.type_field)

    def eventFilter(self, source, event):
        if source == self.search_button:
            if event.type() == QEvent.Enter:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #1565C0;  
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 18px;
                        font-weight: bold;
                        padding: 15px;
                    }
                """)
            elif event.type() == QEvent.Leave:
                source.setStyleSheet("""
                    QPushButton {
                        background-color: #2196F3;  
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 18px;
                        font-weight: bold;
                        padding: 15px;
                    }
                """)
        return super().eventFilter(source, event)

    def show_message(self, message):
        if not message:
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()
