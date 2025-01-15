from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QCalendarWidget,
    QHeaderView,
    QSizePolicy
)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont

from controller.controller_appointment_menu import ControllerAppointmentMenu


class ScreenAppointmentMenu(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = ControllerAppointmentMenu(self)

        self.setWindowTitle("Appointments")
        self.setMinimumSize(1000, 700)

        self.main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.date_label = QLabel("Selected Date: None")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.date_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f2f2f2;
            }
        """)
        left_layout.addWidget(self.date_label)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Time", "Patient", "Type", "Actions"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #f2f2f2;
                padding: 10px;
                border: 1px solid #ddd;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                font-size: 14px;
            }
        """)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        left_layout.addWidget(self.table)

        self.find_button = QPushButton("Find Appointment")
        self.find_button.setFixedHeight(50)
        self.find_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
            QPushButton:pressed {
                background-color: #095a9d;
            }
        """)
        self.find_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.find_button.clicked.connect(self.controller.find_appointment_button_clicked)
        left_layout.addWidget(self.find_button)

        right_layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            QCalendarWidget QAbstractItemView::item {
                border: none;
                font-size: 14px;
            }
            QCalendarWidget QAbstractItemView::item:selected {
                background-color: #2196F3;
                color: white;
            }
        """)
        self.calendar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.calendar.setFixedSize(350, 300)
        self.calendar.selectionChanged.connect(self.controller.on_date_selected)
        right_layout.addWidget(self.calendar)

        self.add_button = QPushButton("Add Appointment")
        self.add_button.setFixedHeight(50)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)
        self.add_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.add_button.clicked.connect(self.controller.add_appointment_button_clicked)
        right_layout.addWidget(self.add_button)
        right_layout.addStretch()

        self.main_layout.addLayout(left_layout, 3)
        self.main_layout.addLayout(right_layout, 1)

        self.setLayout(self.main_layout)

        self.calendar.setSelectedDate(QDate.currentDate())
        self.controller.on_date_selected()
