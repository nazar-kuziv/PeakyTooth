from utils.db_connection import DBConnection
from view.screen_admin_doctor import ScreenAdminDoctor
from view.screen_edit_doctor import ScreenEditDoctor


class ControllerAdminDoctor:
    def __init__(self, view):
        self.view = view
        self.db = DBConnection()

    def add_doctor_form(self):
        from view.screen_add_doctor import ScreenAddDoctor
        self.view.main_screen.add_screen_to_stack(ScreenAddDoctor())

    def search_doctors(self):
        try:
            name = self.view.name_field.text()
            surname = self.view.surname_field.text()
            doctors = self.db.search_doctors(name, surname)
            self.view.populate_table(doctors)
        except Exception as e:
            self.view.show_error(f"Error searching doctors: {str(e)}")

    def update_doctor_password(self, doctor_id):
        try:
            self.db.update_doctor_password(doctor_id, "NULL")
        except Exception as e:
            self.view.show_error(f"Error deleting doctor: {str(e)}")

    def doctor_page_click(self):
        self.view.main_screen.add_screen_to_stack(ScreenAdminDoctor(self.view.main_screen))

    def edit_doctor(self, doctor_id):
        self.view.main_screen.add_screen_to_stack(ScreenEditDoctor(self.view.main_screen, doctor_id))
