from PySide6.QtCore import QPoint, QDate, QTime
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget

from utils.environment import Environment

CALENDAR_WIDGET_WIDTH = 312


class DatePicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        input_container = QHBoxLayout()
        input_container.setContentsMargins(0, 0, 0, 0)
        input_container.setSpacing(10)

        self._time_field = QLineEdit(self)
        self._time_field.setPlaceholderText("HH : MM")
        self._time_field.textChanged.connect(self._validate_time_input)
        self._time_field.setFixedHeight(45)
        self._time_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #D0D0D0;
                border-radius: 12px;
                padding: 12px;
                font-size: 18px;
                background-color: #FAFAFA;
                color: #333;
                box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
            }
            QLineEdit::placeholder {
                color: #AAAAAA;
            }
            QLineEdit:focus {
                border: 2px solid #0078D4;
                background-color: #FFFFFF;
            }
        """)

        self._date_field = QLineEdit(self)
        self._date_field.setPlaceholderText("YYYY - MM - DD")
        self._date_field.textChanged.connect(self._validate_date_input)
        self._date_field.setFixedHeight(45)
        self._date_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #D0D0D0;
                border-radius: 12px;
                padding: 12px;
                font-size: 18px;
                background-color: #FAFAFA;
                color: #333;
                box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
            }
            QLineEdit::placeholder {
                color: #AAAAAA;
            }
            QLineEdit:focus {
                border: 2px solid #0078D4;
                background-color: #FFFFFF;
            }
        """)

        self._calendar_toggle = QPushButton()
        self._calendar_toggle.setFixedSize(45, 45)
        self._calendar_toggle.setIcon(QIcon(Environment.resource_path('static/images/calendar.png')))
        self._calendar_toggle.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #D0D0D0;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
            QPushButton:pressed {
                background-color: #E0E0E0;
            }
        """)
        self._calendar_toggle.clicked.connect(self._toggle_calendar_visibility)

        input_container.addWidget(self._time_field, 1)
        input_container.addWidget(self._date_field, 2)
        input_container.addWidget(self._calendar_toggle)

        root_layout.addLayout(input_container)

        self._calendar_widget = QCalendarWidget(self)
        self._calendar_widget.setStyleSheet("""
            QCalendarWidget QWidget {
                alternate-background-color: #F7F7F7;
                selection-background-color: #A0C8FF;
                background-color: white;
                border-radius: 12px;
            }

            QCalendarWidget QToolButton {
                color: black;
                font-size: 13px;
                background-color: #F0F0F0;
                border: none;
                padding: 8px;
                border-radius: 8px;
            }

            QCalendarWidget QToolButton:hover {
                background-color: #E0E0E0;
            }

            QCalendarWidget QHeaderView::section {
                background-color: #F7F7F7;
                color: black;
                font-size: 16px;
            }

            QCalendarWidget QTableView {
                selection-background-color: #A0C8FF;
                border: 1px solid #D0D0D0;
            }

            QCalendarWidget QTableView::item:selected {
                background-color: #0078D4;
                color: white;
                border-radius: 8px;
            }

            QCalendarWidget QTableView {
                transition: all 0.3s ease;
            }
        """)

        self._calendar_widget.setWindowFlags(Qt.Popup)
        self._calendar_widget.setGridVisible(True)
        self._calendar_widget.hide()
        self._calendar_widget.clicked.connect(self._on_date_selected)

        self.setLayout(root_layout)

    def _validate_date_input(self):
        if self._is_date_input_valid():
            self._date_field.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #D0D0D0;
                    border-radius: 12px;
                    padding: 12px;
                    font-size: 18px;
                    background-color: #FAFAFA;
                    color: #333;
                }
            """)
        else:
            self._date_field.setStyleSheet("""
                QLineEdit {
                    border: 2px solid red;
                    border-radius: 12px;
                    padding: 12px;
                    font-size: 18px;
                    background-color: #FFEEEE;
                    color: #333;
                }
            """)

    def _is_date_input_valid(self):
        entered_text = self._date_field.text()

        if not entered_text:
            return True

        parsed_date = QDate.fromString(entered_text, "yyyy-MM-dd")
        return parsed_date.isValid()

    def _validate_time_input(self):
        if self.is_time_input_valid():
            self._time_field.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #D0D0D0;
                    border-radius: 12px;
                    padding: 12px;
                    font-size: 18px;
                    background-color: #FAFAFA;
                    color: #333;
                }
            """)
        else:
            self._time_field.setStyleSheet("""
                QLineEdit {
                    border: 2px solid red;
                    border-radius: 12px;
                    padding: 12px;
                    font-size: 18px;
                    background-color: #FFEEEE;
                    color: #333;
                }
            """)

    def is_time_input_valid(self):
        entered_text = self._time_field.text()

        if not entered_text:
            return True

        parsed_time = QTime.fromString(entered_text, "hh:mm")
        return parsed_time.isValid()

    def _on_date_selected(self, selected_date):
        self._date_field.setText(selected_date.toString("yyyy-MM-dd"))
        self._calendar_widget.hide()

    def _toggle_calendar_visibility(self):
        if self._calendar_widget.isVisible():
            self._calendar_widget.hide()
        else:
            button_position = self._calendar_toggle.mapToGlobal(
                QPoint(self._calendar_toggle.width() - CALENDAR_WIDGET_WIDTH, self._calendar_toggle.height()))
            self._calendar_widget.move(button_position)
            self._calendar_widget.show()

    def get_date(self):
        if not self._is_date_input_valid() or self._date_field.text().strip() == "":
            return None
        return self._date_field.text()

    def get_time(self):
        if not self.is_time_input_valid() or self._time_field.text().strip() == "":
            return None
        return self._time_field.text()
