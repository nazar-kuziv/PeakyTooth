from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QScrollArea

from controller.controller_appointment_details import ControllerAppointmentDetails
from view.widget.button_base import ButtonBase
from view.widget.image_with_header_label_and_button import ImageWithHeaderLabelAndButton
from view.widget.text_edit_with_header_label import TextEditWithHeaderLabel


class ScreenAppointmentDetails(QWidget):
    def __init__(self, main_view, appointment_id=None):
        super().__init__()
        self.setWindowTitle('Appointment Details')
        self.main_view = main_view
        self.controller = ControllerAppointmentDetails(self, appointment_id)

        self.main_layout = QVBoxLayout()

        self.save_btn = ButtonBase('Save')
        self.save_btn.clicked.connect(self.controller.save_appointment_details)
        self.save_btn.setMinimumWidth(100)

        top_layout = QVBoxLayout()
        # noinspection PyUnresolvedReferences
        top_layout.addWidget(self.save_btn, alignment=Qt.AlignRight)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        self.services_field = TextEditWithHeaderLabel('Services', self.controller.get_services())
        self.services_field.setMinimumHeight(200)
        content_layout.addWidget(self.services_field)

        self.symptoms_description_field = TextEditWithHeaderLabel(
            'Symptoms Description', self.controller.get_symptoms_description())
        self.symptoms_description_field.setMinimumHeight(250)
        content_layout.addWidget(self.symptoms_description_field)

        self.mucous_membrane_field = TextEditWithHeaderLabel(
            'Mucous Membrane', self.controller.get_mucous_membrane())
        self.mucous_membrane_field.setMinimumHeight(250)
        content_layout.addWidget(self.mucous_membrane_field)

        self.periodontium_field = TextEditWithHeaderLabel(
            'Periodontium', self.controller.get_periodontium())
        self.periodontium_field.setMinimumHeight(250)
        content_layout.addWidget(self.periodontium_field)

        self.hygiene_field = TextEditWithHeaderLabel(
            'Hygiene', self.controller.get_hygiene())
        self.hygiene_field.setMinimumHeight(250)
        content_layout.addWidget(self.hygiene_field)

        self.oral_additional_info_field = TextEditWithHeaderLabel(
            'Oral Additional Info', self.controller.get_oral_additional_info())
        self.oral_additional_info_field.setMinimumHeight(250)
        content_layout.addWidget(self.oral_additional_info_field)

        self.additional_info_field = TextEditWithHeaderLabel(
            'Additional Info', self.controller.get_additional_info())
        self.additional_info_field.setMinimumHeight(250)
        content_layout.addWidget(self.additional_info_field)

        self.medications_field = TextEditWithHeaderLabel(
            'Medications', self.controller.get_medications())
        self.medications_field.setMinimumHeight(250)
        content_layout.addWidget(self.medications_field)

        pixmap = QPixmap()
        img_bytes = self.controller.get_dental_diagram()
        if img_bytes:
            pixmap.loadFromData(img_bytes)
            self.dental_diagram_field = ImageWithHeaderLabelAndButton(
                'Dental Diagram', pixmap, 'Edit', self.controller.edit_dental_diagram)
            self.dental_diagram_field.setMinimumSize(951, 629)
        else:
            self.dental_diagram_field = ImageWithHeaderLabelAndButton(
                'Dental Diagram', None, 'Create', self.controller.edit_dental_diagram)

        content_layout.addWidget(self.dental_diagram_field)

        scroll_area.setWidget(content_widget)

        outer_layout = QVBoxLayout(self)
        outer_layout.addLayout(top_layout)
        outer_layout.addWidget(scroll_area)
        self.setLayout(outer_layout)

    def set_new_pixmap(self, img):
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.dental_diagram_field.setMinimumSize(951, 629)
        self.dental_diagram_field.set_btn_text('Edit')
        self.dental_diagram_field.set_pixmap(pixmap)

    def get_services_text(self):
        return self.services_field.get_text().strip() if self.services_field.get_text().strip() else None

    def get_symptoms_description_text(self):
        return self.symptoms_description_field.get_text().strip() if self.symptoms_description_field.get_text().strip() else None

    def get_mucous_membrane_text(self):
        return self.mucous_membrane_field.get_text().strip() if self.mucous_membrane_field.get_text().strip() else None

    def get_periodontium_text(self):
        return self.periodontium_field.get_text().strip() if self.periodontium_field.get_text().strip() else None

    def get_hygiene_text(self):
        return self.hygiene_field.get_text().strip() if self.hygiene_field.get_text().strip() else None

    def get_oral_additional_info_text(self):
        return self.oral_additional_info_field.get_text().strip() if self.oral_additional_info_field.get_text().strip() else None

    def get_additional_info_text(self):
        return self.additional_info_field.get_text().strip() if self.additional_info_field.get_text().strip() else None

    def get_medications_text(self):
        return self.medications_field.get_text().strip() if self.medications_field.get_text().strip() else None

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', str(message))

    def show_success(self, message):
        QMessageBox.information(self, 'Success', message)
