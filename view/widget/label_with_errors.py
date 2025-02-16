from PySide6 import QtCore
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QWidget, QSizePolicy


class LabelWithErrors(QWidget):
    def __init__(self, label_text, initial_text, validator_foo, default_error_message, can_be_empty=False):
        super().__init__()

        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

        self.setObjectName("LabelWithErrors")

        # noinspection PyUnresolvedReferences
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            #LabelWithErrors {
                background-color: #F5F6F7;
                border-radius: 10px;
                border: 1px solid #D3D3D3;
            }            
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.can_be_empty = can_be_empty
        self.validator_foo = validator_foo
        self.default_error_message = default_error_message

        self.label = QLabel(label_text)
        self.main_layout.addWidget(self.label)
        self.label.setStyleSheet("font-size: 17px")

        self.text = QLineEdit(initial_text)
        self.main_layout.addWidget(self.text)

        self.error = QLabel()
        self.error.setStyleSheet("color: red")
        self.main_layout.addWidget(self.error)

        self.text.textChanged.connect(self.set_error_message_if_not_correct)

    def set_error_message_if_not_correct(self):
        if (not self.can_be_empty) and (self.text.text().strip() == ''):
            self.error.setText('Field cannot be empty')
            self.error.setVisible(True)
            return
        if not self.validator_foo(self.text.text().strip()):
            self.error.setText(self.default_error_message)
            self.error.setVisible(True)
            return
        self.error.setVisible(False)

    def get_text(self):
        return self.text.text().strip()
