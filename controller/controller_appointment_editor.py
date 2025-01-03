from PySide6.QtCore import QDate, QTime

from utils.db_connection import DBConnection


class AppointmentEditorController:
    def __init__(self, view, appointment_id):
        self.view = view
        self.appointment_id = appointment_id
        self.db = DBConnection()

    def load_appointment_details(self):
        # Fetch appointment details from the database
        appointment = self.db.get_appointment_by_id(self.appointment_id).data[0]
        date = QDate.fromString(appointment['date'], "yyyy-MM-dd")
        time = QTime.fromString(appointment['time'], "HH:mm:ss")
        print(time.toString())
        notes = appointment['notes']
        appointment_type = appointment['type']
        patient_name = f"{appointment['patients']['patient_name']} {appointment['patients']['patient_surname']}"

        self.populate_fields(date, time, notes, appointment_type, patient_name)


    def update_appointment(self, date, time, notes, appointment_type):
        pass

    def populate_fields(self, date, time, notes, appointment_type, patient_name):
        self.view.date_field.setDate(date)
        self.view.time_field.setTime(time)
        self.view.notes_field.setPlainText(notes)
        self.view.type_field.setCurrentText(appointment_type)
        self.view.patient_name_label.setText(f"Patient: {patient_name}")

