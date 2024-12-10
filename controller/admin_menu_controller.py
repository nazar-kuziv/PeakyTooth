from view.patient_search import PatientSearchForm


class AdminMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_click(self):
        self.view.main_screen.setCentralWidget(PatientSearchForm(self.view.main_screen))
        self.view.deleteLater()
