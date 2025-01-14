from controller.controller_appointment_form import ControllerAppointmentForm
from utils.db_connection import DBConnection
from utils.user_session import UserSession
from view.screen_appointment_form import ScreenAppointmentForm
from view.screen_edit_patient import ScreenEditPatient


class ControllerPatientInfo:
    def __init__(self, view, patient_id):
        self.view = view
        self.patient_id = patient_id

    def setPatientInfo(self):
        db = DBConnection()
        user_session = UserSession()
        patient = db.get_patient(user_session.organization_id, self.patient_id)

        if patient:
            patient_info = patient[0]  # Assuming the list has one item, get the first one

            self.view.label_patient_name.setText("Name: " + patient_info['patient_name'])
            self.view.label_patient_surname.setText("Surname: " + patient_info["patient_surname"])
            self.view.label_patient_dob.setText(
                "Date fo birth: " + patient_info["date_of_birth"])  # Correct field usage
            self.view.label_patient_sex.setText("Sex: " + patient_info["sex"])
            self.view.label_patient_email.setText("Email: " + patient_info["email"])
            self.view.label_patient_phone.setText("Telephone: " + patient_info["telephone"])
            self.view.label_patient_allergy.setText(
                "Analgesics allergy: " + ("Yes" if patient_info["analgesics_allergy"] else "No"))

    def edit_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenEditPatient(self.view.main_screen, self.patient_id))

    def create_appointment_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(
            ScreenAppointmentForm(self.view.main_screen, self.patient_id, ControllerAppointmentForm))
