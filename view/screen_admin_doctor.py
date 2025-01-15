from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QFrame,
    QMessageBox,
    QRadioButton,
    QButtonGroup,
)


class ScreenAdminDoctor(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.selected_doctor_id = None

        self.setWindowTitle("Doctor Admin Page")
        from controller.controller_admin_doctor import ControllerAdminDoctor

        self.controller = ControllerAdminDoctor(self)

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.form_layout = QFormLayout()

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter doctor's name")
        self.name_field.setFixedHeight(40)
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
        self.form_layout.addRow("Name", self.name_field)

        self.surname_field = QLineEdit()
        self.surname_field.setPlaceholderText("Enter doctor's surname")
        self.surname_field.setFixedHeight(40)
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
        self.form_layout.addRow("Surname", self.surname_field)

        self.search_button = QPushButton("Search")
        self.search_button.setFixedHeight(40)
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1F618D;
            }
            QPushButton:pressed {
                background-color: #154360;
            }
        """)
        self.search_button.clicked.connect(self.controller.search_doctors)
        self.form_layout.addRow(self.search_button)

        self.left_layout = QVBoxLayout()
        self.left_layout.addLayout(self.form_layout)
        self.left_layout.addStretch()
        self.main_layout.addLayout(self.left_layout, stretch=1)

        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.vertical_line)

        self.right_layout = QVBoxLayout()

        self.add_doctor_button = QPushButton("Add Doctor")
        self.add_doctor_button.setFixedHeight(40)
        self.add_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1E8449; 
            }
            QPushButton:pressed {
                background-color: #145A32;
            }
        """)
        self.add_doctor_button.clicked.connect(self.controller.add_doctor_form)
        self.right_layout.addWidget(self.add_doctor_button, alignment=Qt.AlignRight)
        self.right_layout.addSpacing(10)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Surname", "Login", "Select"])
        self.table.horizontalHeader().setStretchLastSection(True)
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
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)
        self.table.setHorizontalHeaderLabels(["Name", "Surname", "Login", "Select"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.right_layout.addWidget(self.table)

        self.edit_doctor_button = QPushButton("Edit Doctor")
        self.edit_doctor_button.setFixedHeight(40)
        self.edit_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:disabled {
                background-color: #A9A9A9;
                color: white;
            }
            QPushButton:hover:enabled {
                background-color: #1F618D; 
            }
            QPushButton:pressed:enabled {
                background-color: #154360;
            }
        """)
        self.edit_doctor_button.setEnabled(False)
        self.edit_doctor_button.clicked.connect(self.edit_selected_doctor)
        self.right_layout.addWidget(self.edit_doctor_button, alignment=Qt.AlignRight)
        self.right_layout.addSpacing(10)

        self.delete_doctor_button = QPushButton("Delete Doctor")
        self.delete_doctor_button.setFixedHeight(40)
        self.delete_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #C0392B;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #A93226;
            }
            QPushButton:pressed {
                background-color: #78281F;
            }
        """)
        self.delete_doctor_button.clicked.connect(self.delete_selected_doctor)
        self.right_layout.addWidget(self.delete_doctor_button, alignment=Qt.AlignRight)
        self.right_layout.addStretch()
        self.main_layout.addLayout(self.right_layout, stretch=3)

        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.setExclusive(True)
        self.controller.search_doctors()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            if source == self.search_button:
                source.setStyleSheet("background-color: #A9A9A9; color: white;")
            elif source == self.add_doctor_button:
                source.setStyleSheet("background-color: #006400; color: white;")
            elif source == self.delete_doctor_button:
                source.setStyleSheet("background-color: #8B0000; color: white;")
            elif source == self.edit_doctor_button:
                source.setStyleSheet("background-color: #00008B; color: white;")
        elif event.type() == QEvent.Leave:
            if source == self.search_button:
                source.setStyleSheet("background-color: #C0C0C0;")
            elif source == self.add_doctor_button:
                source.setStyleSheet("background-color: green; color: white;")
            elif source == self.delete_doctor_button:
                source.setStyleSheet("background-color: red; color: white;")
            elif source == self.edit_doctor_button:
                source.setStyleSheet("background-color: blue; color: white;")
        return super().eventFilter(source, event)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", str(message))

    def populate_table(self, doctors):
        self.table.setColumnCount(4)  # Adjust column count
        self.table.setHorizontalHeaderLabels(["Name", "Surname", "Login", "Select"])  # Adjust headers
        self.table.setRowCount(len(doctors))
        for row, doctor in enumerate(doctors):
            self.table.setItem(row, 0, QTableWidgetItem(doctor["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(doctor["surname"]))
            self.table.setItem(row, 2, QTableWidgetItem(doctor["login"]))

            radio_button = QRadioButton()
            radio_button.doctor_id = doctor["userid"]
            self.radio_button_group.addButton(radio_button, row)
            radio_button.toggled.connect(self.handle_radio_button_toggled)

            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(radio_button)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)

            self.table.setCellWidget(row, 3, widget)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

    def handle_radio_button_toggled(self, checked):
        radio_button = self.sender()
        doctor_id = getattr(radio_button, 'doctor_id', None)
        if doctor_id is not None:
            if checked:
                self.selected_doctor_id = doctor_id
                self.edit_doctor_button.setEnabled(True)
            else:
                self.selected_doctor_id = None
                self.edit_doctor_button.setEnabled(False)
        else:
            self.selected_doctor_id = None
            self.edit_doctor_button.setEnabled(False)

    def edit_selected_doctor(self):
        if self.selected_doctor_id:
            self.controller.edit_doctor(self.selected_doctor_id)
        else:
            self.show_error("No doctor selected for editing.")

    def show_message(self, message):
        QMessageBox.information(self, "Information", message)

    def delete_selected_doctor(self):
        selected_doctor_id = None
        for row in range(self.table.rowCount()):
            widget = self.table.cellWidget(row, 3)
            if widget:
                radio_button = widget.findChild(QRadioButton)
                if radio_button and radio_button.isChecked():
                    selected_doctor_id = radio_button.doctor_id
                    break
        if selected_doctor_id:
            self.controller.delete_doctor_by_id(selected_doctor_id)
            self.show_message("Selected doctor deleted successfully.")
            self.refresh()
        else:
            self.show_error("No doctor selected.")

    def refresh(self):
        self.controller.search_doctors()
        self.table.horizontalHeader().setStretchLastSection(True)
