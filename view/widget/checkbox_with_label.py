from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QCheckBox


class CheckboxWithLabel(QWidget):
    def __init__(self, label_text):
        super().__init__()

        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

        self.setObjectName("CheckableWidget")

        # noinspection PyUnresolvedReferences
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            #CheckableWidget {
                background-color: #F5F6F7;
                border-radius: 10px;
                border: 1px solid #D3D3D3;
            }
            QCheckBox {
                font-size: 17px;
                padding: 5px;
            }
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.checkbox = QCheckBox(label_text)
        self.main_layout.addWidget(self.checkbox)

    def is_checked(self):
        return self.checkbox.isChecked()

    def set_checked(self, state: bool):
        self.checkbox.setChecked(state)

    def get_state(self):
        return self.checkbox.isChecked()
