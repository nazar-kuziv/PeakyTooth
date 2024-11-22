from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QEvent
import sys
from view.admin_patients_page import AdminPatientsPage
from view.add_doctor_page import AddDoctorPage

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Menu")
        self.setFixedSize(500, 400)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #D3D3D3;")


        self.doctors_button = QPushButton("Doctors")
        self.doctors_button.setFixedSize(125, 200)
        self.doctors_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)


        self.patients_button = QPushButton("Patients")
        self.patients_button.setFixedSize(125, 200)
        self.patients_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)
        self.patients_button.clicked.connect(self.open_patients_menu)

        self.add_doctor_button = QPushButton("Add Doctor")
        self.add_doctor_button.setFixedSize(125, 200)
        self.add_doctor_button.setStyleSheet("""
                   background-color: #C0C0C0;
                   border-radius: 10px;
                   font-size: 16px;
               """)
        self.add_doctor_button.clicked.connect(self.add_doctor_form)





        button_layout.addStretch()
        button_layout.addWidget(self.doctors_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.patients_button)
        button_layout.addStretch()
        #button_layout.addSpacing(20)
        button_layout.addWidget(self.add_doctor_button)
        button_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()


        central_widget.setLayout(main_layout)

        self.doctors_button.installEventFilter(self)
        self.patients_button.installEventFilter(self)
        self.add_doctor_button.installEventFilter(self)

    def eventFilter(self, source, event):

        if event.type() == QEvent.Enter:
            if source in (self.doctors_button, self.patients_button,self.add_doctor_button):

                source.setStyleSheet("""
                    background-color: #A9A9A9;
                    border-radius: 10px;
                    font-size: 16px;
                    color: white;
                """)
        elif event.type() == QEvent.Leave:
            if source in (self.patients_button, self.doctors_button,self.add_doctor_button):
                source.setStyleSheet("""
                           background-color: #C0C0C0;
                           border-radius: 10px;
                           font-size: 16px;
                       """)

        return super().eventFilter(source, event)

    def open_patients_menu(self):
        self.setCentralWidget(AdminPatientsPage())

    def add_doctor_form(self):
        self.setCentralWidget(AddDoctorPage())