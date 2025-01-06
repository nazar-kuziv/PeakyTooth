from PySide6.QtWidgets import QMessageBox

from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm


class DentistMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_clicked(self):
        self.view.main_screen.setCentralWidget(NewPatientForm(self.view.main_screen))
        self.view.deleteLater()


    def patient_search_button_clicked(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen))
        self.view.deleteLater()

    def create_appointment_button_clicked(self):
        # Logika dla przycisku "Create Appointment"
        QMessageBox.information(self.view, "Info", "TO DO")

    def delete_appointment_button_clicked(self):
        # Logika dla przycisku "Delete Appointment"
        QMessageBox.information(self.view, "Info", "TO DO")
