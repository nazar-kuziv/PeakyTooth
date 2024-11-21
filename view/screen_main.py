from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QToolBar, QWidget

from view.widget.button_base import ButtonBase


class ScreenMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_menu_bar()

    def set_menu_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(50)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        spacer = QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        btn = ButtonBase('Logout')
        toolbar.addWidget(btn)


    def setCentralWidget(self, widget):
        #TODO get rid of remeining widgets in memory
        super().setCentralWidget(widget)
