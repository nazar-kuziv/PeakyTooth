from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QGroupBox,
    QSizePolicy, QHeaderView, QGridLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from controller.doctors_management_controller import DoctorsManagementController


class DoctorsManagementForm(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = DoctorsManagementController(self)

        self.setWindowTitle("Manage Dentist Accounts")
        self.setMinimumSize(800, 850)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 5, 20, 5)
        self.layout.setSpacing(15)
        self.setLayout(self.layout)

        # Back Button
        self.button_back = QPushButton("Back")
        self.button_back.setFixedSize(100, 40)
        self.button_back.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        self.button_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.button_back, alignment=Qt.AlignLeft)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Login", "Name", "Surname", "Role", "Actions"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(False)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                gridline-color: #ccc;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #f2f2f2;
                padding: 10px;
                border: 1px solid #ddd;
                font-weight: bold;
            }
        """)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.layout.addWidget(self.table)

        # Add Dentist Group
        self.add_group = QGroupBox("Add New Dentist")
        self.add_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        self.add_group_layout = QGridLayout()
        self.add_group_layout.setSpacing(10)
        self.add_group_layout.setContentsMargins(15, 15, 15, 15)

        # Input fields for adding
        self.input_login = self.create_input_row("Login:", "Enter login", 0)
        self.input_password = self.create_input_row("Password:", "Enter password", 1, password=True)
        self.input_name = self.create_input_row("Name:", "Enter name", 2)
        self.input_surname = self.create_input_row("Surname:", "Enter surname", 3)

        self.button_add = QPushButton("Add Dentist")
        self.button_add.setFixedSize(150, 40)
        self.button_add.setStyleSheet("""
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
        self.add_group_layout.addWidget(self.button_add, 4, 1, alignment=Qt.AlignLeft)
        self.button_add.clicked.connect(self.controller.add_dentist)

        self.add_group.setLayout(self.add_group_layout)
        self.layout.addWidget(self.add_group)

        # Edit Dentist Group
        self.edit_group = QGroupBox("Edit Selected Dentist")
        self.edit_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        self.edit_layout = QGridLayout()
        self.edit_layout.setSpacing(10)
        self.edit_layout.setContentsMargins(15, 15, 15, 15)

        # Input fields for editing
        self.edit_login = self.create_edit_input_row("Login:", "Edit login", 0)
        self.edit_name = self.create_edit_input_row("Name:", "Edit name", 1)
        self.edit_surname = self.create_edit_input_row("Surname:", "Edit surname", 2)
        self.edit_password = self.create_edit_input_row("New Password:", "Enter new password", 3, password=True)

        self.button_edit_save = QPushButton("Save Changes")
        self.button_edit_save.setFixedSize(150, 40)
        self.button_edit_save.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e68900;
            }
            QPushButton:pressed {
                background-color: #d67c00;
            }
        """)
        self.edit_layout.addWidget(self.button_edit_save, 4, 1, alignment=Qt.AlignLeft)
        self.button_edit_save.clicked.connect(self.controller.edit_dentist)

        self.edit_group.setLayout(self.edit_layout)
        self.layout.addWidget(self.edit_group)

        self.controller.load_dentists()
        self.table.cellClicked.connect(self.on_table_cell_clicked)

    def create_input_row(self, label_text, placeholder, row, password=False):
        label = QLabel(f"<b>{label_text}</b>")
        label.setStyleSheet("""
            QLabel {
                font-size: 12px;  /* Zwiększony rozmiar czcionki */
                font-weight: bold;
            }
        """)
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        if password:
            input_field.setEchoMode(QLineEdit.Password)
        input_field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px; 
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        self.add_group_layout.addWidget(label, row, 0)
        self.add_group_layout.addWidget(input_field, row, 1)
        return input_field

    def create_edit_input_row(self, label_text, placeholder, row, password=False):
        label = QLabel(f"<b>{label_text}</b>")
        label.setStyleSheet("""
            QLabel {
                font-size: 12px;  /* Zwiększony rozmiar czcionki */
                font-weight: bold;
            }
        """)
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        if password:
            input_field.setEchoMode(QLineEdit.Password)
        input_field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px; 
            }
            QLineEdit:focus {
                border: 1px solid #FF9800;
            }
        """)
        self.edit_layout.addWidget(label, row, 0)
        self.edit_layout.addWidget(input_field, row, 1)
        return input_field

    def display_dentists(self, dentists):
        self.table.setRowCount(len(dentists))
        for row_idx, dentist in enumerate(dentists):
            user_id = dentist['userid']
            role = dentist['role']

            id_item = QTableWidgetItem(str(user_id))
            id_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 0, id_item)

            login_item = QTableWidgetItem(dentist.get('login', ''))
            login_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 1, login_item)

            name_item = QTableWidgetItem(dentist.get('name', ''))
            name_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 2, name_item)

            surname_item = QTableWidgetItem(dentist.get('surname', ''))
            surname_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 3, surname_item)

            role_item = QTableWidgetItem(role)
            role_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 4, role_item)

            delete_button = QPushButton("Delete")
            delete_button.setFixedSize(80, 30)
            delete_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #d32f2f;
                }
                QPushButton:pressed {
                    background-color: #b71c1c;
                }
            """)
            delete_button.setCursor(Qt.PointingHandCursor)
            delete_button.clicked.connect(lambda _, uid=user_id: self.controller.delete_dentist(uid))

            actions_layout = QHBoxLayout()
            actions_layout.addWidget(delete_button)
            actions_layout.setAlignment(Qt.AlignCenter)
            actions_layout.setContentsMargins(0, 0, 0, 0)

            actions_widget = QWidget()
            actions_widget.setLayout(actions_layout)
            self.table.setCellWidget(row_idx, 5, actions_widget)

        self.clear_edit_fields()

    def on_table_cell_clicked(self, row, column):
        user_id_item = self.table.item(row, 0)
        login_item = self.table.item(row, 1)
        name_item = self.table.item(row, 2)
        surname_item = self.table.item(row, 3)

        if user_id_item:
            self.edit_user_id = int(user_id_item.text())
        if login_item:
            self.edit_login.setText(login_item.text())
        if name_item:
            self.edit_name.setText(name_item.text())
        if surname_item:
            self.edit_surname.setText(surname_item.text())

        self.edit_password.clear()

    def clear_edit_fields(self):
        self.edit_user_id = None
        self.edit_login.clear()
        self.edit_name.clear()
        self.edit_surname.clear()
        self.edit_password.clear()

    def clear_add_fields(self):
        self.ad_user_id = None
        self.input_login.clear()
        self.input_name.clear()
        self.input_password.clear()
        self.input_surname.clear()

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.setStyleSheet("""
            QMessageBox {
                font-size: 14px;
            }
        """)
        msg.exec()

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message, QMessageBox.Ok, QMessageBox.Ok)

    def go_back(self):
        from view.admin_menu import AdminMenu
        self.main_screen.setCentralWidget(AdminMenu(self.main_screen))
        self.deleteLater()
