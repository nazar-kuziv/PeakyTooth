from PySide6.QtCore import QTime

from utils.db_connection import DBConnection
from view.appointment_editor_screen import AppointmentEditorForm


class AppointmentInfoController:
    def __init__(self, view, appointment_id):
        self.view = view
        self.appointment_id = appointment_id

    def setAppointmentInfo(self):
        # Fetch appointment info and update the labels
        db = DBConnection()
        appointment = db.get_appointment_by_id(self.appointment_id).data[0]
        print(appointment)
        self.view.label_appointment_id.setText(f"ID: {appointment['id']}")
        self.view.label_patient_name.setText(f"Patient: {appointment['patients']['patient_name']} {appointment['patients']['patient_surname']}")
        self.view.label_date.setText(f"Date: {appointment['date']}")
        time = QTime.fromString(appointment['time'], "HH:mm:ss").toString("HH:mm")
        self.view.label_time.setText(f"Time: {time}")
        self.view.label_type.setText(f"Type: {appointment['type']}")
        self.view.label_notes.setText(f"Notes: {appointment['notes']}")

    def edit_appointment_button_clicked(self):
        self.view.main_screen.setCentralWidget(AppointmentEditorForm(self.view.main_screen, self.appointment_id))
        self.view.deleteLater()

    def delete_appointment_button_clicked(self):
        # Open reschedule appointment form
        pass

