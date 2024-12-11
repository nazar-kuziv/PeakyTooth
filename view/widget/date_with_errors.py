from PySide6 import QtCore
from PySide6.QtWidgets import QVBoxLayout, QLabel, QDateEdit, QWidget, QSizePolicy


class DateWithErrors(QWidget):
    def __init__(self, label_text, initial_date, validator_foo, default_error_message, can_be_empty=False):
        super().__init__()

        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

        self.setObjectName("LabelWithDateErrors")

        # noinspection PyUnresolvedReferences
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            #LabelWithDateErrors {
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

        self.date_edit = QDateEdit()

        # noinspection PyUnresolvedReferences
        initial_date = QtCore.QDate.fromString(initial_date, QtCore.Qt.ISODate)
        self.date_edit.setDate(initial_date)
        self.date_edit.setDisplayFormat('yyyy-MM-dd')
        self.date_edit.setCalendarPopup(True)
        self.main_layout.addWidget(self.date_edit)

        self.error = QLabel()
        self.error.setStyleSheet("color: red")
        self.main_layout.addWidget(self.error)

        self.date_edit.dateChanged.connect(self.set_error_message_if_not_correct)

    def set_error_message_if_not_correct(self):
        if not self.can_be_empty and not self.date_edit.date().isValid():
            self.error.setText('Field cannot be empty')
            self.error.setVisible(True)
            return

        # noinspection PyUnresolvedReferences
        date_text = self.date_edit.date().toString(QtCore.Qt.ISODate)
        if not self.validator_foo(date_text):
            self.error.setText(self.default_error_message)
            self.error.setVisible(True)
            return

        self.error.setVisible(False)

    def get_date(self):
        # noinspection PyUnresolvedReferences
        return self.date_edit.date().toString(QtCore.Qt.ISODate)
