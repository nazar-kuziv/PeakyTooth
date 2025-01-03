import bcrypt
from PySide6.QtWidgets import QMessageBox, QPushButton, QTableWidgetItem

from utils.db_connection import DBConnection
from utils.user_session import UserSession
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData


class DoctorsManagementController:
    def __init__(self, view):
        self.view = view
        try:
            self.db = DBConnection()
        except DBUnableToConnect as e:
            self.view.show_error(str(e))

    def load_dentists(self):
        """
        Pobiera wszystkich użytkowników o roli 'Dentist' (dla organizacji zalogowanego admina)
        i wyświetla w tabeli
        """
        try:
            user_session = UserSession()
            organization_id = user_session.organization_id
            dentists = self.db.get_dentists(organization_id)
            self.view.display_dentists(dentists)
        except DBUnableToGetData as e:
            self.view.show_error(f"Error retrieving dentist data: {str(e)}")

    def add_dentist(self):
        """
        Dodaje nowego dentystę na podstawie danych w polach formularza
        """
        login = self.view.input_login.text().strip()
        password = self.view.input_password.text().strip()
        name = self.view.input_name.text().strip()
        surname = self.view.input_surname.text().strip()

        # Walidacja
        if not login or not password or not name or not surname:
            self.view.show_message("All fields (Login, Password, Name, Surname) are required!")
            return

        # Hash hasła
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

        # Ustawienia roli
        role = "Dentist"
        user_session = UserSession()
        organization_id = user_session.organization_id

        # Zapis w bazie
        message = self.db.create_dentist_account(login, hashed_password, name, surname, role, organization_id)
        self.view.show_message(message)
        self.load_dentists()  # odświeżenie tabeli

    def delete_dentist(self, user_id):
        """
        Usuwa użytkownika o wskazanym user_id
        """
        reply = QMessageBox.question(
            self.view,
            "Delete Dentist",
            "Are you sure you want to delete this dentist?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            message = self.db.delete_dentist_account(user_id)
            self.view.show_message(message)
            self.load_dentists()

    def edit_dentist(self):
        """
        Edycja danych dentysty (po wciśnięciu przycisku 'Save Changes')
        """
        user_id = self.view.edit_user_id
        if user_id is None:
            self.view.show_message("No user selected for editing!")
            return

        new_login = self.view.edit_login.text().strip()
        new_name = self.view.edit_name.text().strip()
        new_surname = self.view.edit_surname.text().strip()
        new_password = self.view.edit_password.text().strip()

        if not new_login or not new_name or not new_surname:
            self.view.show_message("Login, Name, and Surname must not be empty!")
            return

        updated_data = {
            "login": new_login,
            "name": new_name,
            "surname": new_surname
        }

        # jeśli admin wprowadził nowe hasło, to je haszujemy
        if new_password:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt).decode('utf-8')
            updated_data["password"] = hashed_password

        message = self.db.update_dentist_account(user_id, updated_data)
        self.view.show_message(message)
        self.load_dentists()

        # wyczyść pola edycji
        self.view.clear_edit_fields()
