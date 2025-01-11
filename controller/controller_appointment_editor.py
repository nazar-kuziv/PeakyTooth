from PySide6.QtCore import QDate, QTime

from utils.db_connection import DBConnection
from utils.user_session import UserSession


class AppointmentEditorController:
    def __init__(self, view, appointment_id):
        self.view = view
        self.appointment_id = appointment_id

    def setAppointmentForm(self):
        db = DBConnection()
        user_session = UserSession()
        appointment = db.get_appointment_by_id(self.appointment_id)
        appointment = appointment.data[0]  # Get the first appointment in the list
        self.view.patient_name_label.setText(
            "Patient: " + appointment['patients']['patient_name'] + " " + appointment['patients']['patient_surname'])

        self.view.date_field.setDate(QDate.fromString(appointment['date'], "yyyy-MM-dd"))
        self.view.time_field.setTime(QTime.fromString(appointment['time'], "hh:mm:ss"))
        self.view.notes_field.setText(appointment['notes'])
        self.view.type_field.setCurrentText(appointment['type'])

        self.view.date_field.setDate(QDate.currentDate())
        self.view.time_field.setTime(QTime.currentTime())

    def createAppointment(self):
        db = DBConnection()
        date = self.view.date_field.text(),
        time = self.view.time_field.text(),
        notes = self.view.notes_field.toPlainText(),
        type = self.view.type_field.currentText()
        response = db.update_appointment(self.appointment_id, date, time, type, notes)
        if (response):
            self.view.show_message(response)
        else:
            self.view.show_message("Error")

