from PySide6 import QtCore
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QSizePolicy, QHBoxLayout

from view.widget.button_base import ButtonBase


class ImageWithHeaderLabelAndButton(QWidget):
    def __init__(self, label_text, pixmap, btn_text, btn_func):
        super().__init__()

        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

        self.setObjectName("ImageWithHeaderLabel")

        # noinspection PyUnresolvedReferences
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            #ImageWithHeaderLabel {
                background-color: #F5F6F7;
                border-radius: 10px;
                border: 1px solid #D3D3D3;
            }            
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.label_and_button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.label_and_button_layout)

        self.label = QLabel(label_text)
        self.label_and_button_layout.addWidget(self.label)
        self.label.setStyleSheet("font-size: 17px; font-weight: bold;")

        self.btn = ButtonBase(btn_text)
        self.btn.clicked.connect(btn_func)
        self.btn.setMaximumWidth(100)
        self.label_and_button_layout.addWidget(self.btn)

        self.img = QLabel()
        if pixmap:
            self.img.setPixmap(pixmap)
        self.main_layout.addWidget(self.img)

    def set_pixmap(self, pixmap):
        self.img.setPixmap(pixmap)

    def set_btn_text(self, text: str):
        self.btn.setText(text)