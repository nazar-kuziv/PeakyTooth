import sys

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QCalendarWidget, QTableWidget, QTableWidgetItem,
    QWidget, QHeaderView, QApplication
)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from controller.controller_appointment_menu import AppointmentMenuController


class AppointmentMenu(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = AppointmentMenuController(self)

        self.setWindowTitle("Appointments")
        self.setMinimumSize(800, 600)

        self.main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.date_label = QLabel("Selected Date: None")
        self.date_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.date_label)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Time", "Patient", "Type", ""])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        left_layout.addWidget(self.table)

        self.find_button = QPushButton("Find Appointment")
        left_layout.addWidget(self.find_button)
        self.find_button.clicked.connect(self.controller.find_appointment_button_clicked)

        right_layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setFixedSize(300, 200)
        self.calendar.selectionChanged.connect(self.controller.on_date_selected)
        right_layout.addWidget(self.calendar)

        self.add_button = QPushButton("Add Appointment")
        right_layout.addWidget(self.add_button)
        right_layout.addStretch()
        self.add_button.clicked.connect(self.controller.add_appointment_button_clicked)

        self.main_layout.addLayout(left_layout, 1)
        self.main_layout.addLayout(right_layout)

        self.setLayout(self.main_layout)

        self.calendar.setSelectedDate(QDate.currentDate())
        self.controller.on_date_selected()



