from view.patient_search import PatientSearchForm
from view.doctors_management_form import DoctorsManagementForm


class AdminMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_click(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen))
        self.view.deleteLater()

    def doctors_button_click(self):
        self.view.main_screen.setCentralWidget(DoctorsManagementForm(self.view.main_screen))
        self.view.deleteLater()
