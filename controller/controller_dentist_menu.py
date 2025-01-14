from controller.controller_patient_search import ControllerPatientSearch
from view.screen_appointments_menu import ScreenAppointmentMenu
from view.screen_new_patient import ScreenNewPatient
from view.screen_patient_search import ScreenPatientSearch


class ControllerDentistMenu:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenNewPatient(self.view.main_screen))

    def patient_search_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenPatientSearch(self.view.main_screen, ControllerPatientSearch))

    def appointments_button_clicked(self):
        self.view.main_screen.add_screen_to_stack(ScreenAppointmentMenu(self.view.main_screen))
