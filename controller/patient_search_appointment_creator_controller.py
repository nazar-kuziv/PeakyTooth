from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.user_session import UserSession
from view.appointment_form import AppointmentForm


class PatientSearchAppointmentCreatorController:
    def __init__(self, view):
        self.view = view

        try:
            self.db = DBConnection()
        except DBUnableToConnect as e:
            self.view.show_error(e)

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self.view)
        msg.setIcon(QMessageBox.Information)  # You can use Information, Warning, or Critical
        msg.setText(message)

        msg.exec()

    def select_patient(self, patient_id):
        self.view.main_screen.setCentralWidget(AppointmentForm(self.view.main_screen, patient_id))

    def display_patients(self, patients):
        self.view.table.setRowCount(len(patients))
        for row, patient in enumerate(patients):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(patient["id"])))
            self.view.table.setItem(row, 1, QTableWidgetItem(patient["patient_name"]))
            self.view.table.setItem(row, 2, QTableWidgetItem(patient["patient_surname"]))  # First Name
            self.view.table.setItem(row, 3, QTableWidgetItem(patient["date_of_birth"]))  # Last Name
            self.view.table.setItem(row, 4, QTableWidgetItem(patient["telephone"]))

            select_button = QPushButton("Select")

            select_button.clicked.connect(self.make_select_patient_method(patient["id"]))

            self.view.table.setCellWidget(row, 5, select_button)

    def make_select_patient_method(self, patient_id):

        def select():
            self.select_patient(patient_id)

        return select

    def search_patients(self):
        try:
            user_session = UserSession()
            organization_id = user_session.organization_id

            # Query the database for matching patients
            patients = self.db.find_patients(self.view.id_field.text(), self.view.name_field.text(),
                                             self.view.surname_field.text(), organization_id)
            if not patients:
                self.display_patients([])
                self.show_message("No patients found.")
            else:
                self.display_patients(patients)
        except DBUnableToGetData as e:
            self.show_message(f"Error retrieving patient data: {str(e)}")
        except Exception as e:
            self.show_message(f"Unexpected error: {str(e)}")


