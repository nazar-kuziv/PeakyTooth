from view.new_patient_form import NewPatientForm
from view.patient_search import PatientSearchForm

class DentistMenuController:
    def __init__(self, view):
        self.view = view  # <--- to jest DentistMenu, które ma self.main_screen

    def patients_button_clicked(self):
        for i in range(self.view.main_screen.stacked_widget.count()):
            if isinstance(self.view.main_screen.stacked_widget.widget(i), NewPatientForm):
                self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
                self.view.main_screen.stacked_widget.setCurrentIndex(i)
                self.view.main_screen.update_back_button()  # jeśli masz taką metodę w ScreenMain
                return
        form = NewPatientForm(self.view.main_screen)
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        self.view.main_screen.stacked_widget.addWidget(form)
        self.view.main_screen.stacked_widget.setCurrentWidget(form)
        self.view.main_screen.update_back_button()  # jeśli masz taką metodę w ScreenMain

    def patient_search_button_clicked(self):
        for i in range(self.view.main_screen.stacked_widget.count()):
            if isinstance(self.view.main_screen.stacked_widget.widget(i), PatientSearchForm):
                self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
                self.view.main_screen.stacked_widget.setCurrentIndex(i)
                self.view.main_screen.update_back_button()
                return
        form = PatientSearchForm(self.view.main_screen)
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        self.view.main_screen.stacked_widget.addWidget(form)
        self.view.main_screen.stacked_widget.setCurrentWidget(form)
        self.view.main_screen.update_back_button()

    def create_appointment_button_clicked(self):
        # Przykładowo, jeśli chcesz iść do innego widoku:
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        # tutaj dodaj logikę tworzenia appointment
        self.view.main_screen.update_back_button()

    def delete_appointment_button_clicked(self):
        self.view.main_screen.history_stack.append(self.view.main_screen.stacked_widget.currentIndex())
        # tutaj dodaj logikę usuwania appointment
        self.view.main_screen.update_back_button()
