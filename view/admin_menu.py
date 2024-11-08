from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QEvent
import sys

class MainWindow(QMainWindow):
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


        button_layout.addStretch()
        button_layout.addWidget(self.doctors_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.patients_button)
        button_layout.addStretch()


        self.exit_button = QPushButton("Exit")
        self.exit_button.setFixedSize(60, 30)
        self.exit_button.setStyleSheet("""
            background-color: #FF5C5C;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 12px;
        """)


        main_layout.addWidget(self.exit_button, alignment=Qt.AlignRight)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()


        central_widget.setLayout(main_layout)

        self.doctors_button.installEventFilter(self)
        self.patients_button.installEventFilter(self)
        self.exit_button.installEventFilter(self)


    def eventFilter(self, source, event):

        if event.type() == QEvent.Enter:
            if source in (self.doctors_button, self.patients_button, self.exit_button):

                source.setStyleSheet("""
                    background-color: #A9A9A9;
                    border-radius: 10px;
                    font-size: 16px;
                    color: white;
                """ if source != self.exit_button else """
                    background-color: #D9534F;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 5px;
                    font-size: 12px;
                """)

        elif event.type() == QEvent.Leave:
            if source in (self.doctors_button, self.patients_button, self.exit_button):

                source.setStyleSheet("""
                    background-color: #C0C0C0;
                    border-radius: 10px;
                    font-size: 16px;
                """ if source != self.exit_button else """
                    background-color: #FF5C5C;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 5px;
                    font-size: 12px;
                """)

        return super().eventFilter(source, event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
