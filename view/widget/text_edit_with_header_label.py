from PySide6 import QtCore
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QSizePolicy, QTextEdit


class TextEditWithHeaderLabel(QWidget):
    def __init__(self, label_text, initial_text):
        super().__init__()

        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

        self.setObjectName("TextEditWithHeaderLabel")

        # noinspection PyUnresolvedReferences
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            #TextEditWithHeaderLabel {
                background-color: #F5F6F7;
                border-radius: 10px;
                border: 1px solid #D3D3D3;
            }            
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.label = QLabel(label_text)
        self.main_layout.addWidget(self.label)
        self.label.setStyleSheet("font-size: 17px; font-weight: bold;")

        self.text = QTextEdit(str(initial_text) if initial_text else "")
        self.main_layout.addWidget(self.text)

    def get_text(self):
        return self.text.toPlainText().strip()
