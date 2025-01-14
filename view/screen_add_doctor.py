from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFormLayout,
    QWidget, QMessageBox,
)

from controller.contoller_add_doctor import ControllerAddDoctor


class ScreenAddDoctor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New patient form")
        self.controller = ControllerAddDoctor(self)

        self.form_layout = QFormLayout()

        self.setForm()

    def setForm(self):
        self.name_field = QLineEdit()
        self.form_layout.addRow("Name:", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Surname:", self.surname_field)

        self.login_field = QLineEdit()
        self.form_layout.addRow("Login:", self.login_field)

        self.pass_field = QLineEdit()
        # noinspection PyUnresolvedReferences
        self.pass_field.setEchoMode(QLineEdit.Password)
        self.form_layout.addRow("Password:", self.pass_field)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.addDoctor)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button)
        self.setLayout(main_layout)

    def show_message(self, message):
        if message == '':
            return
        msg = QMessageBox(self)
        # noinspection PyUnresolvedReferences
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)

        msg.exec()

    def addDoctor(self):
        self.controller.add_doctor(
            self.name_field.text(),
            self.surname_field.text(),
            self.pass_field.text(),
            self.login_field.text()
        )
