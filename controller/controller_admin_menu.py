from controller.controller_patient_search import ControllerPatientSearch
from view.screen_add_doctor import ScreenAddDoctor
from view.screen_admin_doctor import ScreenAdminDoctor
from view.screen_patient_search import ScreenPatientSearch


class ControllerAdminMenu:
    def __init__(self, view):
        self.view = view

    def patients_button_click(self):
        self.view.main_screen.add_screen_to_stack(ScreenPatientSearch(self.view.main_screen, ControllerPatientSearch))

    def add_doctor_form(self):
        self.view.main_screen.add_screen_to_stack(ScreenAddDoctor())

    def doctor_page_click(self):
        self.view.main_screen.add_screen_to_stack(ScreenAdminDoctor(self.view.main_screen))
