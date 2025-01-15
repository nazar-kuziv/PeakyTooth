from PySide6.QtWidgets import (
    QFormLayout, QDateEdit, QTimeEdit, QComboBox, QTextEdit,
    QPushButton, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QMessageBox
)


class ScreenAppointmentForm(QWidget):
    def __init__(self, main_screen, patient_appointment_id, controller):
        super().__init__()

        self.main_screen = main_screen
        self.controller = controller(self, patient_appointment_id)

        self.setMinimumSize(500, 400)
        self.setWindowTitle("Appointment Form")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        self.patient_info_layout = QHBoxLayout()

        self.patient_name_label = QLabel("Patient Name: [Placeholder]")
        self.patient_name_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                background-color: #f2f2f2;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        self.name_surname_layout = QHBoxLayout()
        self.name_surname_layout.addWidget(self.patient_name_label)
        self.name_surname_layout.setSpacing(5)

        self.patient_info_layout.addLayout(self.name_surname_layout)

        self.main_layout.addLayout(self.patient_info_layout)

        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(12)

        self.date_field = QDateEdit()
        self.date_field.setCalendarPopup(True)
        self.date_field.setDisplayFormat("yyyy-MM-dd")
        self.date_field.setStyleSheet("""
            QDateEdit {
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
            }
            QDateEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.form_layout.addRow("Date:", self.date_field)

        self.time_field = QTimeEdit()
        self.time_field.setDisplayFormat("HH:mm")
        self.time_field.setStyleSheet("""
            QTimeEdit {
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
            }
            QTimeEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.form_layout.addRow("Time:", self.time_field)

        self.notes_field = QTextEdit()
        self.notes_field.setPlaceholderText("Enter any notes for the appointment...")
        self.notes_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.notes_field.setStyleSheet("""
            QTextEdit {
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QTextEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.form_layout.addRow("Notes:", self.notes_field)

        self.type_field = QComboBox()
        self.type_field.addItems(["Consultation", "Procedure", "Follow-up", "Emergency"])
        self.type_field.setStyleSheet("""
            QComboBox {
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
            }
            QComboBox:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.form_layout.addRow("Type:", self.type_field)

        self.main_layout.addLayout(self.form_layout)

        self.create_button = QPushButton("Apply")
        self.create_button.setFixedHeight(50)
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
            QPushButton:pressed {
                background-color: #095a9d;
            }
        """)
        self.create_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.create_button.clicked.connect(self.controller.createAppointment)

        self.main_layout.addWidget(self.create_button)

        self.setLayout(self.main_layout)

        self.controller.setAppointmentForm()

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStyleSheet("font-size: 14px;")
        msg.exec()
