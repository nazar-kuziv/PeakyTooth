from view.patient_search import PatientSearchForm
from view.doctors_management_form import DoctorsManagementForm


class AdminMenuController:
    def __init__(self, view):
        self.view = view

    def patients_button_click(self):
        for i in range(self.view.main_screen.stacked_widget.count()):
            if isinstance(self.view.main_screen.stacked_widget.widget(i), PatientSearchForm):
                self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
                self.view.main_screen.stacked_widget.setCurrentIndex(i)
                return
        form = PatientSearchForm(self.view.main_screen)
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        self.view.main_screen.stacked_widget.addWidget(form)
        self.view.main_screen.stacked_widget.setCurrentWidget(form)

    def doctors_button_click(self):
        for i in range(self.view.main_screen.stacked_widget.count()):
            if isinstance(self.view.main_screen.stacked_widget.widget(i), DoctorsManagementForm):
                self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
                self.view.main_screen.stacked_widget.setCurrentIndex(i)
                return
        form = DoctorsManagementForm(self.view.main_screen)
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        self.view.main_screen.stacked_widget.addWidget(form)
        self.view.main_screen.stacked_widget.setCurrentWidget(form)
