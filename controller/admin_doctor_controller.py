# controller/admin_doctor_controller.py

from utils.db_connection import DBConnection
from view.admin_doctor_page import AdminDoctorPage


class DoctorController:
    def __init__(self, view):
        self.view = view
        self.db = DBConnection()

    def add_doctor_form(self):
        from view.add_doctor_page import AddDoctorPage
        self.view.main_screen.setCentralWidget(AddDoctorPage())
        self.view.deleteLater()

    def get_doctors(self):
        try:
            doctors = self.db.get_doctors()
            return doctors
        except Exception as e:
            self.view.show_error(f"Error fetching doctors: {str(e)}")
            return []

    def search_doctors(self):
        try:
            name = self.view.name_field.text()
            surname = self.view.surname_field.text()
          #  us_id = self.view.id_field.text()
            doctors = self.db.search_doctors(name, surname)
            self.view.populate_table(doctors)
            #self.table.resizeColumnsToContents()
        except Exception as e:
            self.view.show_error(f"Error searching doctors: {str(e)}")


    def delete_selected_doctors(self, doctor_ids):
        try:
            for doctor_id in doctor_ids:
                self.db.delete_doctor_by_id(doctor_id)
            self.view.show_message("Selected doctors deleted successfully.")
            self.view.populate_table(self.get_doctors())  # Refresh the table
        except Exception as e:
            self.view.show_error(f"Error deleting doctors: {str(e)}")

    def doctor_page_click(self):
        self.view.main_screen.setCentralWidget(AdminDoctorPage(self.view.main_screen))
        self.view.deleteLater()