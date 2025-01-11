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
        self.setWindowTitle('PeakyTooth')
        self.controller = ControllerMain(self)
        # noinspection PyUnresolvedReferences
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.set_tool_bar()

    def set_tool_bar(self):
        toolbar = QToolBar()
        # noinspection PyUnresolvedReferences
        toolbar.setContextMenuPolicy(Qt.NoContextMenu)
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(55)
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
        # noinspection PyUnresolvedReferences
        widget_user_info.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        layout_user_info = QHBoxLayout()
        # noinspection PyUnresolvedReferences
        # layout_user_info.setAlignment(Qt.AlignCenter)
        widget_user_info.setLayout(layout_user_info)

        svg_img = QSvgWidget(Environment.resource_path(
            'static/images/logo_admin.svg')) if self.controller.get_user_role() == 'Admin' else QSvgWidget(
            Environment.resource_path('static/images/logo_dentist.svg'))
        # noinspection PyUnresolvedReferences
        svg_img.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
        svg_img.setMaximumWidth(75)

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
        label_username.setMinimumHeight(30)

        layout_username_and_organization.addWidget(label_username)

        layout_username_and_organization.addStretch(1)
  
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

        self.showMaximized()

    def setCentralWidget(self, widget):
        super().setCentralWidget(widget)
