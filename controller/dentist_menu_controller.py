from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm


class DentistMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.deleteLater()
        self.view.main_screen.setCentralWidget(NewPatientForm(self.view.main_screen))

    def patient_search_button_clicked(self):
        self.view.deleteLater()
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen))