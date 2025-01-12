from PySide6.QtWidgets import (
    QMainWindow, QToolBar, QLabel, QStackedWidget,
    QHBoxLayout, QVBoxLayout, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6 import QtWidgets

from utils.environment import Environment
from utils.user_session import UserSession
from view.widget.button_base import ButtonBase
from controller.controller_main import ControllerMain

class ScreenMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = ControllerMain(self)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.history_stack = []
        self.set_tool_bar()
        self.setWindowTitle("Main Screen")

        # Dodanie głównego widgetu do stacked_widget
        self.main_widget = self.create_main_widget()
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.setCurrentWidget(self.main_widget)

        self.update_back_button()

        self.stacked_widget.currentChanged.connect(self.on_current_changed)

    def set_tool_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(60)
        toolbar.setMaximumHeight(60)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        widget_user_info = QWidget()
        widget_user_info.setObjectName('widget_user_info')
        layout_user_info = QHBoxLayout()
        layout_user_info.setContentsMargins(0, 0, 0, 0)
        widget_user_info.setLayout(layout_user_info)

        if self.controller.get_user_role() == 'Admin':
            svg_img = QSvgWidget(Environment.resource_path('static/images/logo_admin.svg'))
        else:
            svg_img = QSvgWidget(Environment.resource_path('static/images/logo_dentist.svg'))
        svg_img.setFixedSize(40, 40)
        layout_user_info.addWidget(svg_img)

        layout_username_and_organization = QVBoxLayout()
        layout_username_and_organization.setContentsMargins(10, 0, 10, 0)

        label_username = QLabel(self.controller.get_user_name_and_surname())
        label_username.setStyleSheet(
            "font-size: 16px; font-weight: bold; color: #333333;"
        )
        label_username.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout_username_and_organization.addWidget(label_username)

        label_organization = QLabel(self.controller.get_user_organization())
        label_organization.setStyleSheet(
            "font-size: 12px; font-style: italic; color: #777777;"
        )
        label_organization.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout_username_and_organization.addWidget(label_organization)

        layout_user_info.addLayout(layout_username_and_organization)
        toolbar.addWidget(widget_user_info)

        spacer = QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        self.btn_back = ButtonBase('Back')
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6; 
                color: white; 
                border: none; 
                border-radius: 10px; 
                padding: 10px 20px; 
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
            QPushButton:pressed {
                background-color: #707B7C;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #ecf0f1;
            }
        """)

        self.btn_back.setFixedSize(80, 40)
        self.btn_back.clicked.connect(self.on_back_clicked)
        toolbar.addWidget(self.btn_back)

        btn_logout = ButtonBase('Logout && Exit')
        btn_logout.setStyleSheet(
            "background-color: #E74C3C; color: white; border: none; "
            "border-radius: 10px; padding: 10px 20px; font-size: 14px;"
        )
        btn_logout.setFixedSize(140, 40)
        btn_logout.clicked.connect(ControllerMain.logout)
        toolbar.addWidget(btn_logout)

    def on_back_clicked(self):
        if self.history_stack:
            previous_index = self.history_stack.pop()
            self.stacked_widget.setCurrentIndex(previous_index)
            self.update_back_button()

    def update_back_button(self):
        self.btn_back.setEnabled(len(self.history_stack) > 0)

    def on_current_changed(self, index):
        self.update_back_button()

    def create_main_widget(self):
        w = QWidget()
        layout = QVBoxLayout()
        w.setLayout(layout)

        return w