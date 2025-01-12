from PySide6.QtCore import QTime
from PySide6.QtWidgets import QPushButton, QTableWidgetItem

from controller.patient_search_appointment_creator_controller import PatientSearchAppointmentCreatorController
from utils.db_connection import DBConnection
from utils.user_session import UserSession
from view.appointment_search import AppointmentSearchForm
from view.patient_search import PatientSearchForm
from view.screen_appointment_info import AppointmentInfoScreen


class AppointmentMenuController:
    def __init__(self, view):
        self.view = view
        self.db = DBConnection()

    def update_table(self):
        self.view.table.setRowCount(0)  # Clear previous contents
        user_session = UserSession()
        appointments = self.db.get_appointments_by_date(
            user_session.user_id,
            self.view.calendar.selectedDate().toString('yyyy-MM-dd')
        ).data

        for appointment in appointments:
            patient_name = appointment['patients']['patient_name']
            patient_surname = appointment['patients']['patient_surname']
            appointment_type = appointment['type']
            appointment_time = QTime.fromString(appointment['time'], "HH:mm:ss").toString("HH:mm")
            appointment_id = appointment['id']

            # Insert a new row in the table
            row_position = self.view.table.rowCount()
            self.view.table.insertRow(row_position)

            # Set the table data
            self.view.table.setItem(row_position, 0, QTableWidgetItem(str(appointment_id)))
            self.view.table.setItem(row_position, 1, QTableWidgetItem(appointment_time))
            self.view.table.setItem(row_position, 2, QTableWidgetItem(patient_name + ' ' + patient_surname))
            self.view.table.setItem(row_position, 3, QTableWidgetItem(appointment_type))

            # Add a button in the last column
            action_button = QPushButton("Select")
            action_button.clicked.connect(self.make_action_button_method(appointment_id))
            self.view.table.setCellWidget(row_position, 4, action_button)

    def make_action_button_method(self, appointment_id):
        def action():
            self.perform_action_for_appointment(appointment_id)

        return action

    def perform_action_for_appointment(self, appointment_id):
        self.view.main_screen.add_screen_to_stack(AppointmentInfoScreen(self.view.main_screen, appointment_id))

    def get_selected_date(self):
        return self.view.calendar.selectedDate().toString("yyyy-MM-dd")

    def on_date_selected(self):
        selected_date = self.get_selected_date()
        self.view.date_label.setText(f"Selected Date: {selected_date}")
        self.update_table()

    def add_appointment_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(
            PatientSearchForm(self.view.main_screen, PatientSearchAppointmentCreatorController))

    def find_appointment_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(AppointmentSearchForm(self.view.main_screen))
