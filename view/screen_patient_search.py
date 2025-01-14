from PySide6.QtWidgets import (
    QVBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QWidget, QFormLayout, QSizePolicy
)


class ScreenPatientSearch(QWidget):
    def __init__(self, main_screen, controller):
        super().__init__()
        self.main_screen = main_screen

        self.setWindowTitle("Patient Search")
        self.controller = controller(self)

        self.form_layout = QFormLayout()

        self.id_field = QLineEdit()
        self.form_layout.addRow("Patient ID", self.id_field)

        self.name_field = QLineEdit()
        self.form_layout.addRow("Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Surname:", self.surname_field)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.controller.search_patients)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.search_button)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Date of Birth", "Telephone", ""])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.main_layout.addWidget(self.table)

        self.main_layout.setStretch(0, 0)
        self.main_layout.setStretch(1, 0)
        self.main_layout.setStretch(2, 1)

        self.setLayout(self.main_layout)

        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
