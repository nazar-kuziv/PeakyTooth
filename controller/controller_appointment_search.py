from PySide6.QtCore import QTime
from PySide6.QtWidgets import QTableWidgetItem, QPushButton

from utils.db_connection import DBConnection
from utils.user_session import UserSession
from view.screen_appointment_info import ScreenAppointmentInfo


class ControllerAppointmentSearch:
    def __init__(self, view):
        self.view = view

    def search_appointments(self):
        self.view.table.clearContents()
        self.view.table.setRowCount(0)
        db = DBConnection()
        if self.view.name_field.text().strip() != '':
            patient_name = self.view.name_field.text().strip()
        else:
            patient_name = None
        if self.view.surname_field.text().strip() != '':
            patient_surname = self.view.surname_field.text().strip()
        else:
            patient_surname = None

        date_from = self.view.date_time_from_field.get_date()
        date_to = self.view.date_time_to_field.get_date()

        time_from = self.view.date_time_from_field.get_time()
        time_to = self.view.date_time_to_field.get_time()

        if self.view.type_field.currentText() == "-":
            visit_type = None
        else:
            visit_type = self.view.type_field.currentText()
        user_session = UserSession()
        appointments = db.get_appointments_with_filter(user_session.user_id, patient_name, patient_surname,
                                                       date_from, date_to, time_from, time_to, visit_type)

        for appointment in appointments:
            patient_name = appointment["patients"]["patient_name"]
            patient_surname = appointment["patients"]["patient_surname"]

            appointment_type = appointment['type']
            appointment_date = appointment['date']
            appointment_time = QTime.fromString(appointment['time'], "HH:mm:ss").toString("HH:mm")
            appointment_id = appointment['id']

            # Insert a new row in the table
            row_position = self.view.table.rowCount()
            self.view.table.insertRow(row_position)

            # Set the table data
            self.view.table.setItem(row_position, 0, QTableWidgetItem(str(appointment_id)))
            self.view.table.setItem(row_position, 1, QTableWidgetItem(patient_name + ' ' + patient_surname))
            self.view.table.setItem(row_position, 2, QTableWidgetItem(appointment_date))
            self.view.table.setItem(row_position, 3, QTableWidgetItem(appointment_time))
            self.view.table.setItem(row_position, 4, QTableWidgetItem(appointment_type))

            # Add a button in the last column
            action_button = QPushButton("Select")
            action_button.clicked.connect(self.make_action_button_method(appointment_id))
            self.view.table.setCellWidget(row_position, 5, action_button)

    def make_action_button_method(self, appointment_id):
        def action():
            self.perform_action_for_appointment(appointment_id)

        return action

    def perform_action_for_appointment(self, appointment_id):
        self.view.main_screen.add_screen_to_stack(ScreenAppointmentInfo(self.view.main_screen, appointment_id))
