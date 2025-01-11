# screen_main.py

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QMainWindow, QToolBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox
)

from controller.controller_main import ControllerMain
from utils.environment import Environment
from view.widget.button_base import ButtonBase


class ScreenMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = ControllerMain(self)
        self.set_tool_bar()
        self.setCentralWidget(self.create_main_widget())

    def set_tool_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(60)
        toolbar.setMaximumHeight(60)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        widget_user_info = QWidget()
        widget_user_info.setObjectName('widget_user_info')
        widget_user_info.setStyleSheet("""
            #widget_user_info {
                border: none;
                padding: 10px;
            }
        """)

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
        label_username.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333333;
            }
        """)
        label_username.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout_username_and_organization.addWidget(label_username)

        label_organization = QLabel(self.controller.get_user_organization())
        label_organization.setStyleSheet("""
            QLabel {
                font-size: 12px;
                font-style: italic;
                color: #777777;
            }
        """)
        label_organization.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout_username_and_organization.addWidget(label_organization)

        layout_user_info.addLayout(layout_username_and_organization)

        toolbar.addWidget(widget_user_info)

        spacer = QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        logout_widget = QWidget()
        logout_layout = QHBoxLayout()
        logout_layout.setContentsMargins(0, 0, 20, 0)
        logout_widget.setLayout(logout_layout)

        # --- PRZYCISK BACK ---
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
                background-color: #bdc3c7; /* jaśniejszy szary */
                color: #ecf0f1;           /* jasny napis */
            }
        """)
        self.btn_back.setFixedSize(80, 40)
        self.btn_back.clicked.connect(self.on_back_clicked)
        logout_layout.addWidget(self.btn_back, alignment=Qt.AlignLeft | Qt.AlignVCenter)

        # --- PRZYCISK LOGOUT & EXIT ---
        btn_logout = ButtonBase('Logout && Exit')
        btn_logout.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
            QPushButton:pressed {
                background-color: #A93226;
            }
        """)
        btn_logout.setFixedSize(140, 40)
        btn_logout.clicked.connect(ControllerMain.logout)
        logout_layout.addWidget(btn_logout, alignment=Qt.AlignLeft | Qt.AlignVCenter)

        toolbar.addWidget(logout_widget)

    def setCentralWidget(self, widget: QWidget):

        super().setCentralWidget(widget)
        if hasattr(widget, 'go_back') and callable(widget.go_back):
            self.btn_back.setEnabled(True)
        else:
            self.btn_back.setEnabled(False)

    def on_back_clicked(self):
        current_widget = self.centralWidget()
        if hasattr(current_widget, 'go_back') and callable(current_widget.go_back):
            current_widget.go_back()
        else:
            QMessageBox.information(self, "Info", "Brak obsługi cofania w tym widoku.")

    def create_main_widget(self):
        w = QWidget()
        return w
