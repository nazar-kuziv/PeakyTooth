import base64

from utils.db_connection import DBConnection
from utils.exceptions.cant_find_appointment import CantFindAppointment
from utils.user_session import UserSession
from view.screen_mouthe_visualisation import ScreenMouseVisualisation


class ControllerAppointmentDetails:
    def __init__(self, view, appointment_id):
        self.view = view
        self.appointment_id = appointment_id
        self.current_appointment_details_data = None
        self.mouse_wisualisation_window = None
        self.new_dental_diagram = None
        self.db = DBConnection()
        if self.db.is_appointment_exsist(UserSession().organization_id, appointment_id):
            self.current_appointment_details_data = self._get_current_appointment_details_data(self.appointment_id)
        else:
            self.view.show_error("Cannot find the appointment.")
            raise CantFindAppointment()

    def _get_current_appointment_details_data(self, appointment_id):
        try:
            return self.db.get_appointment_details(UserSession().organization_id, appointment_id)
        except Exception as e:
            self.view.show_error(e)

    def get_services(self):
        try:
            return self.current_appointment_details_data[0]['services']
        except Exception:
            return None

    def get_symptoms_description(self):
        try:
            return self.current_appointment_details_data[0]['symptoms_description']
        except Exception:
            return None

    def get_mucous_membrane(self):
        try:
            return self.current_appointment_details_data[0]['mucous_membrane']
        except Exception:
            return None

    def get_periodontium(self):
        try:
            return self.current_appointment_details_data[0]['periodontium']
        except Exception:
            return None

    def get_hygiene(self):
        try:
            return self.current_appointment_details_data[0]['hygiene']
        except Exception:
            return None

    def get_oral_additional_info(self):
        try:
            return self.current_appointment_details_data[0]['oral_additional_info']
        except Exception:
            return None

    def get_dental_diagram(self):
        try:
            return base64.b64decode(self.current_appointment_details_data[0]['dental_diagram'])
        except Exception:
            return None

    def get_additional_info(self):
        try:
            return self.current_appointment_details_data[0]['additional_info']
        except Exception:
            return None

    def get_medications(self):
        try:
            return self.current_appointment_details_data[0]['medications']
        except Exception:
            return None

    def edit_dental_diagram(self):
        if not self.mouse_wisualisation_window or not self.mouse_wisualisation_window.isVisible():
            self.mouse_wisualisation_window = ScreenMouseVisualisation(self.save_new_dental_diagram_and_change_pixmap,
                                                                       self.new_dental_diagram if self.new_dental_diagram else self.get_dental_diagram())
            self.mouse_wisualisation_window.show()
        else:
            self.mouse_wisualisation_window.activateWindow()

    def save_new_dental_diagram_and_change_pixmap(self, new_img):
        try:
            self.view.set_new_pixmap(new_img)
            self.new_dental_diagram = new_img
            self.mouse_wisualisation_window.close()
        except Exception as e:
            print(f'An error occurred while saving the new dental diagram: {str(e)}')
            self.view.show_error('Smth went wrong please try again')

    def save_appointment_details(self):
        if self.current_appointment_details_data:
            try:
                self.db.alter_appointment_details_using_id(self.appointment_id, self.view.get_services_text(),
                                                           self.view.get_symptoms_description_text(),
                                                           self.view.get_mucous_membrane_text(),
                                                           self.view.get_periodontium_text(),
                                                           self.view.get_hygiene_text(),
                                                           self.view.get_oral_additional_info_text(),
                                                           self.new_dental_diagram if self.new_dental_diagram else self.get_dental_diagram(),
                                                           self.view.get_additional_info_text(),
                                                           self.view.get_medications_text())
                self.view.show_success('Appointment details have been successfully updated')
            except Exception as e:
                print(f'An error occurred while altering the appointment details: {str(e)}')
                self.view.show_error('Smth went wrong please try again')
        else:
            try:
                self.db.insert_appointment_details(self.appointment_id, self.view.get_services_text(),
                                                   self.view.get_symptoms_description_text(),
                                                   self.view.get_mucous_membrane_text(),
                                                   self.view.get_periodontium_text(),
                                                   self.view.get_hygiene_text(),
                                                   self.view.get_oral_additional_info_text(),
                                                   self.new_dental_diagram if self.new_dental_diagram else self.get_dental_diagram(),
                                                   self.view.get_additional_info_text(),
                                                   self.view.get_medications_text())
                self.current_appointment_details_data = self._get_current_appointment_details_data(self.appointment_id)
                self.view.show_success('Appointment details have been successfully added')
            except Exception as e:
                print(f'An error occurred while inserting the appointment details: {str(e)}')
                self.view.show_error('Smth went wrong please try again')
