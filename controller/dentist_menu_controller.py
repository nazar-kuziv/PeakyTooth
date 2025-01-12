from controller.patient_search_controller import PatientSearchController
from view.appointments_menu import AppointmentMenu
from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm


class DentistMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(NewPatientForm(self.view.main_screen))

    def patient_search_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(PatientSearchForm(self.view.main_screen, PatientSearchController))

    def appointments_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(AppointmentMenu(self.view.main_screen))
