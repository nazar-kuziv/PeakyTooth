from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout

from controller.controller_edit_patient import ControllerEditPatient
from view.widget.button_base import ButtonBase
from view.widget.checkbox_with_label import CheckboxWithLabel
from view.widget.date_with_errors import DateWithErrors
from view.widget.label_with_errors import LabelWithErrors


class ScreenEditPatient(QWidget):
    def __init__(self, main_view, patient_id):
        super().__init__()
        self.main_view = main_view
        self.controller = ControllerEditPatient(self, patient_id)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # noinspection PyUnresolvedReferences
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.name_field = LabelWithErrors('Name', self.controller.get_patient_name(),
                                          self.controller.is_name_surname_valid,
                                          'Name must contain only alphabetic characters')
        self.main_layout.addWidget(self.name_field)

        self.surname_field = LabelWithErrors('Surname', self.controller.get_patient_surname(),
                                             self.controller.is_name_surname_valid,
                                             'Surname must contain only alphabetic characters')
        self.main_layout.addWidget(self.surname_field)

        self.date_of_birth_field = DateWithErrors('Date of birth', self.controller.get_patient_date_of_birth(),
                                                  self.controller.is_date_valid,
                                                  'Date of birth must be a valid date and not in the future or before 1900')
        self.main_layout.addWidget(self.date_of_birth_field)

        self.email_field = LabelWithErrors('Email', self.controller.get_patient_email(), self.controller.is_email_valid,
                                           'Email must be a valid email format (e.g., example@mail.com)')
        self.main_layout.addWidget(self.email_field)

        self.telephone_field = LabelWithErrors('Telephone', self.controller.get_patient_phone_number(),
                                               self.controller.is_phone_number_valid,
                                               'Telephone must be a valid phone number, optionally starting with a +, and up to 15 digits')
        self.main_layout.addWidget(self.telephone_field)

        self.allergy_checkbox = CheckboxWithLabel('Analgesics allergy')
        self.allergy_checkbox.set_checked(self.controller.get_patient_analgesics_allergy())
        self.main_layout.addWidget(self.allergy_checkbox)

        self.submit_button = ButtonBase('Submit')
        self.submit_button.clicked.connect(self.submit)
        self.main_layout.addWidget(self.submit_button)

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

    def submit(self):
        response = self.controller.alter_patient_data(self.name_field.get_text(), self.surname_field.get_text(),
                                                      self.date_of_birth_field.get_date(),
                                                      self.allergy_checkbox.get_state(),
                                                      self.telephone_field.get_text(), self.email_field.get_text())
        if response:
            QMessageBox.information(self, 'Success', 'Patient data updated successfully')
