from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QMainWindow, QToolBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy

from controller.controller_main import ControllerMain
from utils.environment import Environment
from view.widget.button_base import ButtonBase


class ScreenMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = ControllerMain(self)
        self.set_tool_bar()

    def set_tool_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(50)
        toolbar.setMaximumHeight(75)
        # noinspection PyUnresolvedReferences
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        # Create user info widget
        widget_user_info = QWidget()

        widget_user_info.setObjectName('widget_user_info')
        widget_user_info.setStyleSheet("""
                #widget_user_info {
                    border: 1px solid black;
                    border-radius: 10px;
                    padding: 10px;
                    margin-bottom: 5px;
                }
            """)

        layout_user_info = QHBoxLayout()
        # noinspection PyUnresolvedReferences
        layout_user_info.setAlignment(Qt.AlignCenter)
        widget_user_info.setLayout(layout_user_info)

        svg_img = QSvgWidget(Environment.resource_path(
            'static/images/logo_admin.svg')) if self.controller.get_user_role() == 'Admin' else QSvgWidget(
            Environment.resource_path('static/images/logo_dentist.svg'))
        svg_img.setFixedSize(30, 30)
        layout_user_info.addWidget(svg_img)

        layout_username_and_organization = QVBoxLayout()

        layout_username_and_organization.addSpacing(5)

        label_username = QLabel(self.controller.get_user_name_and_surname())
        label_username.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                }
            """)
        # noinspection PyUnresolvedReferences
        label_username.setAlignment(Qt.AlignCenter)
        # noinspection PyUnresolvedReferences
        label_username.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout_username_and_organization.addWidget(label_username)

        label_organization = QLabel(self.controller.get_user_organization())
        label_organization.setStyleSheet("""
                QLabel {
                    font-size: 12px;
                    font-style: italic;
                }
            """)
        layout_username_and_organization.addWidget(label_organization)

        layout_username_and_organization.addSpacing(5)

        layout_user_info.addLayout(layout_username_and_organization)

        toolbar.addWidget(widget_user_info)

        spacer = QWidget()
        # noinspection PyUnresolvedReferences
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        btn = ButtonBase('Logout && Exit')
        btn.clicked.connect(ControllerMain.logout)
        toolbar.addWidget(btn)

    def setCentralWidget(self, widget):
        # TODO get rid of remeining widgets in memory
        super().setCentralWidget(widget)
