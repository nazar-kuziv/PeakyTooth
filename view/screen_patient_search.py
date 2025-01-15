from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QLabel, QPushButton, QTableWidget, \
    QHeaderView, QSizePolicy, QMessageBox


class ScreenPatientSearch(QWidget):
    def __init__(self, main_screen, controller):
        super().__init__()
        self.main_screen = main_screen

        self.setWindowTitle("Patient Search")
        self.controller = controller(self)

        self.form_layout = QGridLayout()
        self.form_layout.setContentsMargins(15, 15, 15, 15)
        self.form_layout.setSpacing(10)

        self.id_field = QLineEdit()
        self.id_field.setPlaceholderText("Enter Patient ID")
        self.id_field.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        id_label = QLabel("<b>Patient ID:</b>")
        id_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
        """)
        id_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addWidget(id_label, 0, 0)
        self.form_layout.addWidget(self.id_field, 0, 1)

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter Name")
        self.name_field.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        name_label = QLabel("<b>Name:</b>")
        name_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
        """)
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addWidget(name_label, 1, 0)
        self.form_layout.addWidget(self.name_field, 1, 1)

        self.surname_field = QLineEdit()
        self.surname_field.setPlaceholderText("Enter Surname")
        self.surname_field.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        surname_label = QLabel("<b>Surname:</b>")
        surname_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
        """)
        surname_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addWidget(surname_label, 2, 0)
        self.form_layout.addWidget(self.surname_field, 2, 1)

        self.search_button = QPushButton("Search")
        self.search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.search_button.setMinimumHeight(40)
        self.search_button.setStyleSheet("""
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
        self.search_button.clicked.connect(self.controller.search_patients)

        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.search_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Date of Birth", "Telephone", "Select"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #f2f2f2;
                padding: 10px;
                border: 1px solid #ddd;
                font-weight: bold;
            }
        """)

        self.main_layout.addWidget(self.table)

        self.main_layout.setStretch(0, 0)
        self.main_layout.setStretch(1, 0)
        self.main_layout.setStretch(2, 1)

        self.setLayout(self.main_layout)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStyleSheet("font-size: 14px;")
        msg.exec()
