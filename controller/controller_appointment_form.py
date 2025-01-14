from PySide6.QtCore import QDate, QTime

from utils.db_connection import DBConnection
from utils.user_session import UserSession


class ControllerAppointmentForm:
    def __init__(self, view, patient_id):
        self.view = view
        self.patient_id = patient_id

    def setAppointmentForm(self):
        db = DBConnection()
        user_session = UserSession()
        patient = db.get_patient(user_session.organization_id, self.patient_id)
        patient_info = patient[0]
        self.view.patient_name_label.setText("Patient: " + patient_info['patient_name'] + " " + patient_info['patient_surname'])
        self.view.date_field.setDate(QDate.currentDate())
        self.view.time_field.setTime(QTime.currentTime())

    def createAppointment(self):
        user_session = UserSession()
        appointment_data = {
            "patient_id": self.patient_id,
            "dentist_id": user_session.user_id,
            "date": self.view.date_field.text(),
            "time": self.view.time_field.text(),
            "notes": self.view.notes_field.toPlainText(),
            "type": self.view.type_field.currentText()
        }
        db = DBConnection()
        response = db.create_appointment(appointment_data)
        if(response):
            self.view.show_message(response)
        else:
            self.view.show_message("Error")