from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QEvent
import sys

class AdminPatientsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Patiens Menu")
        self.setFixedSize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        central_widget.setStyleSheet("background-color: #D3D3D3;")
        self.patient_del_button = QPushButton("delete patient")
        self.patient_del_button.setFixedSize(125, 200)
        self.patient_del_button.setStyleSheet("""
            background-color: #C0C0C0;
            border-radius: 10px;
            font-size: 16px;
        """)


        button_layout.addStretch()
        button_layout.addWidget(self.patient_del_button)
        button_layout.addSpacing(20)


        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)



    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            if source in (self.patient_del_button):
                source.setStyleSheet("""
                    background-color: #A9A9A9;
                    border-radius: 10px;
                    font-size: 16px;
                    color: white;
                """)
        elif event.type() == QEvent.Leave:
            if source in (self.patient_del_button):
                source.setStyleSheet("""
                    background-color: #C0C0C0;
                    border-radius: 10px;
                    font-size: 16px;
                """)
        return super().eventFilter(source, event)