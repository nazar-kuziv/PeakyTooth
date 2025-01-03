from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QGroupBox
)
from PySide6.QtCore import Qt, QSize

from controller.doctors_management_controller import DoctorsManagementController


class DoctorsManagementForm(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.controller = DoctorsManagementController(self)

        self.setWindowTitle("Manage Dentist Accounts")

        # Layout główny
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # --- PRZYCISK BACK ---
        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.button_back)
        # ---------------------

        # Tabela z listą dentystów
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Login", "Name", "Surname", "Role", "Actions"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.layout.addWidget(self.table)

        # Formularz do dodawania nowego dentysty
        self.add_group = QGroupBox("Add New Dentist")
        self.add_group_layout = QFormLayout()

        self.input_login = QLineEdit()
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_name = QLineEdit()
        self.input_surname = QLineEdit()

        self.add_group_layout.addRow("Login:", self.input_login)
        self.add_group_layout.addRow("Password:", self.input_password)
        self.add_group_layout.addRow("Name:", self.input_name)
        self.add_group_layout.addRow("Surname:", self.input_surname)

        self.button_add = QPushButton("Add Dentist")
        self.button_add.clicked.connect(self.controller.add_dentist)
        self.add_group_layout.addRow("", self.button_add)

        self.add_group.setLayout(self.add_group_layout)
        self.layout.addWidget(self.add_group)

        # Sekcja edycji wybranego dentysty
        self.edit_group = QGroupBox("Edit Selected Dentist")
        self.edit_layout = QFormLayout()

        self.edit_user_id = None
        self.edit_login = QLineEdit()
        self.edit_name = QLineEdit()
        self.edit_surname = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)

        self.edit_layout.addRow("Login:", self.edit_login)
        self.edit_layout.addRow("Name:", self.edit_name)
        self.edit_layout.addRow("Surname:", self.edit_surname)
        self.edit_layout.addRow("New Password:", self.edit_password)

        self.button_edit_save = QPushButton("Save Changes")
        self.button_edit_save.clicked.connect(self.controller.edit_dentist)
        self.edit_layout.addRow("", self.button_edit_save)

        self.edit_group.setLayout(self.edit_layout)
        self.layout.addWidget(self.edit_group)

        # Załadowanie listy dentystów
        self.controller.load_dentists()

        # Reakcja na kliknięcie wiersza w tabeli (wypełnienie pól edycji)
        self.table.cellClicked.connect(self.on_table_cell_clicked)

    def display_dentists(self, dentists):
        """
        Wyświetla pobranych dentystów w tabeli
        """
        self.table.setRowCount(len(dentists))
        for row_idx, dentist in enumerate(dentists):
            user_id = dentist['userid']
            role = dentist['role']

            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user_id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(dentist.get('login', '')))
            self.table.setItem(row_idx, 2, QTableWidgetItem(dentist.get('name', '')))
            self.table.setItem(row_idx, 3, QTableWidgetItem(dentist.get('surname', '')))
            self.table.setItem(row_idx, 4, QTableWidgetItem(role))

            # Przycisk DELETE
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, uid=user_id: self.controller.delete_dentist(uid))

            actions_layout = QHBoxLayout()
            actions_layout.addWidget(delete_button)
            actions_layout.setContentsMargins(0, 0, 0, 0)

            actions_widget = QWidget()
            actions_widget.setLayout(actions_layout)
            self.table.setCellWidget(row_idx, 5, actions_widget)

        self.clear_edit_fields()

    def on_table_cell_clicked(self, row, column):
        """
        Gdy klikniemy wiersz w tabeli, wypełniamy pola edycji danymi wybranego użytkownika
        """
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

        self.edit_password.clear()  # hasło zawsze puste w polu do edycji

    def clear_edit_fields(self):
        """
        Czyści pola edycji
        """
        self.edit_user_id = None
        self.edit_login.clear()
        self.edit_name.clear()
        self.edit_surname.clear()
        self.edit_password.clear()

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

    def go_back(self):
        """
        Obsługa przycisku 'Back' - powrót do AdminMenu
        """
        # Importujemy AdminMenu lokalnie (w momencie wywołania tej funkcji)
        from view.admin_menu import AdminMenu
        self.main_screen.setCentralWidget(AdminMenu(self.main_screen))
        self.deleteLater()
