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
        self.setCentralWidget(self.create_main_widget())  # Dodanie centralnego widgetu

    def set_tool_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setMinimumHeight(60)
        toolbar.setMaximumHeight(60)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        # Create user info widget
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

        svg_img = QSvgWidget(Environment.resource_path(
            'static/images/logo_admin.svg')) if self.controller.get_user_role() == 'Admin' else QSvgWidget(
            Environment.resource_path('static/images/logo_dentist.svg'))
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

        # Styled Logout Button
        btn = ButtonBase('Logout && Exit')
        btn.setStyleSheet("""
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
        btn.setFixedSize(140, 40)
        btn.clicked.connect(ControllerMain.logout)

        # Adding margin to prevent touching the edge
        logout_widget = QWidget()
        logout_layout = QHBoxLayout()
        logout_layout.setContentsMargins(0, 0, 20, 0)  # Right margin
        logout_layout.addWidget(btn, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        logout_widget.setLayout(logout_layout)
        toolbar.addWidget(logout_widget)

    def create_main_widget(self):
        """Creates the central widget layout with buttons centered."""
        central_widget = QWidget()
        layout = QVBoxLayout()  # Vertical layout for centering
        layout.setAlignment(Qt.AlignCenter)  # Align buttons to the center
        layout.setContentsMargins(0, 0, 0, 0)

        # Example buttons
        doctors_button = ButtonBase('Doctors')
        doctors_button.setFixedSize(200, 50)
        doctors_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1C6396;
            }
        """)

        patients_button = ButtonBase('Patients')
        patients_button.setFixedSize(200, 50)
        patients_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1C6396;
            }
        """)

        layout.addWidget(doctors_button, alignment=Qt.AlignHCenter)
        layout.addSpacing(20)  # Space between buttons
        layout.addWidget(patients_button, alignment=Qt.AlignHCenter)

        central_widget.setLayout(layout)
        return central_widget

    def setCentralWidget(self, widget):
        """Override for setting the central widget."""
        super().setCentralWidget(widget)
