from controller.patient_search_controller import PatientSearchController
from view.add_doctor_page import AddDoctorPage
from view.admin_doctor_page import AdminDoctorPage
from view.patient_search import PatientSearchForm


class AdminMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_click(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen, PatientSearchController))
        self.view.deleteLater()

    def add_doctor_form(self):
        self.view.main_screen.setCentralWidget(AddDoctorPage())
        self.view.deleteLater()

    def doctor_page_click(self):
        self.view.main_screen.setCentralWidget(AdminDoctorPage(self.view.main_screen))
        self.view.deleteLater()






