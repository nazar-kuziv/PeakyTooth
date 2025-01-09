from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm
from view.edit_doctor_page import EditDoctorPage


class DentistMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.main_screen.setCentralWidget(NewPatientForm(self.view.main_screen))
        self.view.deleteLater()


    def patient_search_button_clicked(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen))
        self.view.deleteLater()



