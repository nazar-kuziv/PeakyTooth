from controller.patient_search_appointment_creator_controller import PatientSearchAppointmentCreatorController
from controller.patient_search_controller import PatientSearchController
from view.appointments_menu import AppointmentMenu
from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm


class DentistMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.main_screen.setCentralWidget(NewPatientForm(self.view.main_screen))
        self.view.deleteLater()


    def patient_search_button_clicked(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen, PatientSearchController))
        self.view.deleteLater()

    def appointments_button_clicked(self):
        self.view.main_screen.setCentralWidget(AppointmentMenu(self.view.main_screen))
        self.view.deleteLater()
