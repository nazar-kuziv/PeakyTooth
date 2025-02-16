from PySide6.QtCore import QTime

from controller.controller_appointment_editor import ControllerAppointmentEditor
from utils.db_connection import DBConnection
from view.screen_appointment_form import ScreenAppointmentForm
from view.screen_appointment_details import ScreenAppointmentDetails
from view.screen_pdf import ScreenPdf


class ControllerAppointmentInfo:
    def __init__(self, view, appointment_id):
        self.view = view
        self.appointment_id = appointment_id

    def setAppointmentInfo(self):
        # Fetch appointment info and update the labels
        db = DBConnection()
        appointment = db.get_appointment_by_id(self.appointment_id).data[0]
        self.view.label_appointment_id.setText(f"ID: {appointment['id']}")
        self.view.label_patient_name.setText(f"Patient: {appointment['patients']['patient_name']} {appointment['patients']['patient_surname']}")
        self.view.label_date.setText(f"Date: {appointment['date']}")
        time = QTime.fromString(appointment['time'], "HH:mm:ss").toString("HH:mm")
        self.view.label_time.setText(f"Time: {time}")
        self.view.label_type.setText(f"Type: {appointment['type']}")
        self.view.label_notes.setText(f"Notes: {appointment['notes']}")

    def edit_appointment_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenAppointmentForm(self.view.main_screen, self.appointment_id, ControllerAppointmentEditor))
        

    def add_details_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenAppointmentDetails(self.view.main_screen, self.appointment_id))
        

    def see_appointment_details_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenPdf(self.appointment_id))
        

