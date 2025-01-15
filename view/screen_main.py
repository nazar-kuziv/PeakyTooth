from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QToolBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, \
    QSizePolicy

from controller.controller_main import ControllerMain
from utils.environment import Environment
from view.screen_admin_doctor import ScreenAdminDoctor
from view.screen_appointment_info import ScreenAppointmentInfo
from view.screen_full_patient_info import ScreenPatientInfo
from view.widget.button_base import ButtonBase


class ScreenMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PeakyTooth')
        self.setMinimumSize(1024, 576)

        self.controller = ControllerMain(self)

        self.stack_widget = QStackedWidget()
        self.setCentralWidget(self.stack_widget)

        self.set_tool_bar()

    def set_tool_bar(self):
        self.toolbar = QToolBar()
        # noinspection PyUnresolvedReferences
        self.toolbar.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolbar.setMovable(False)
        self.toolbar.setMinimumHeight(55)
        self.toolbar.setMaximumHeight(75)
        # noinspection PyUnresolvedReferences
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

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

        self.toolbar.addWidget(widget_user_info)

        spacer = QWidget()
        # noinspection PyUnresolvedReferences
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbar.addWidget(spacer)

        logout_btn = ButtonBase('Logout && Exit')
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FF6347;
                color: white;
            }
        """)
        logout_btn.clicked.connect(ControllerMain.logout)

        self.back_btn = ButtonBase('Back')
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #C0C0C0;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #87CEFA;
                color: white;
            }
        """)
        self.back_btn.clicked.connect(self.navigate_to_previous_screen)
        self.back_btn.setEnabled(False)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        button_layout.addWidget(logout_btn)
        button_layout.addWidget(self.back_btn)

        button_container = QWidget()
        button_container.setLayout(button_layout)
        self.toolbar.addWidget(button_container)

        self.showMaximized()

    def add_screen_to_stack(self, screen: QWidget):
        if self.stack_widget.count() == 1:
            self.back_btn.setEnabled(True)
        self.stack_widget.addWidget(screen)
        self.stack_widget.setCurrentWidget(screen)

    def navigate_to_previous_screen(self):
        current_index = self.stack_widget.currentIndex()
        if current_index > 0:
            if isinstance(self.stack_widget.widget(current_index - 1), ScreenAppointmentInfo) or isinstance(
                    self.stack_widget.widget(current_index - 1), ScreenPatientInfo) or isinstance(
                self.stack_widget.widget(current_index - 1), ScreenAdminDoctor):
                # noinspection PyUnresolvedReferences
                self.stack_widget.widget(current_index - 1).refresh()
            self.stack_widget.setCurrentIndex(current_index - 1)
            self.stack_widget.removeWidget(self.stack_widget.widget(current_index))
        if self.stack_widget.count() == 1:
            self.back_btn.setEnabled(False)
