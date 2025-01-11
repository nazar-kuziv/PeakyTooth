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
        input_container.setSpacing(0)

        self._time_field = QLineEdit(self)
        self._time_field.setPlaceholderText("hh:mm")
        self._time_field.textChanged.connect(self._validate_time_input)
        self._time_field.setStyleSheet("""
            QLineEdit {
                color: black;
            }
            QLineEdit::placeholder {
                color: gray;
                opacity: 1;
            }
        """)

        self._date_field = QLineEdit(self)
        self._date_field.setPlaceholderText("yyyy-MM-dd")
        self._date_field.textChanged.connect(self._validate_date_input)
        self._date_field.setStyleSheet("""
            QLineEdit { 
                color: black;  
            } 
            QLineEdit::placeholder { 
                color: gray;  
                opacity: 1;  
            }
        """)

        self._calendar_toggle = QPushButton()
        self._calendar_toggle.setFixedSize(40, 40)
        self._calendar_toggle.setIcon(QIcon(Environment.resource_path('static/images/calendar.png')))
        self._calendar_toggle.setStyleSheet(
            """
                        QPushButton {
                            background-color: white;
                        }
                        QPushButton:hover {
                            background-color: darkgray;
                        }
            """
        )
        self._calendar_toggle.clicked.connect(self._toggle_calendar_visibility)

        input_container.addWidget(self._time_field, 1)
        input_container.addWidget(self._date_field, 2)
        input_container.addWidget(self._calendar_toggle)

        root_layout.addLayout(input_container)

        self._calendar_widget = QCalendarWidget(self)
        self._calendar_widget.setStyleSheet(
            """
                        QCalendarWidget QWidget {
                            alternate-background-color: #f0f0f0;
                            selection-background-color: #A0C8FF;
                            background-color: white;
                        }

                        QCalendarWidget QToolButton {
                            color: black; 
                            font-size: 11px;
                            background-color: #f0f0f0;
                            border: none;
                            padding: 5px;
                        }

                        QCalendarWidget QToolButton:hover {
                            background-color: #d0d0d0; 
                        }

                        QCalendarWidget QToolButton {
                            transition: color 0.3s ease, background-color 0.3s ease;
                        }

                        QCalendarWidget QToolButton::right-arrow {
                            image: url(right-arrow.png); 
                        }

                        QCalendarWidget QToolButton::left-arrow {
                            image: url(left-arrow.png); 
                        }

                        QCalendarWidget QTableView QHeaderView::section {
                            background-color: #f0f0f0;
                            color: black;
                            font-size: 16px;
                        }

                        QCalendarWidget QTableView {
                            selection-background-color: #A0C8FF;
                            border: 1px solid #d0d0d0;
                        }

                        QCalendarWidget QTableView::item:selected {
                            background-color: #A0C8FF; 
                            color: white; 
                        }

                        QCalendarWidget QTableView {
                            transition: all 0.3s ease;
                        }
            """
        )
        # noinspection PyUnresolvedReferences
        self._calendar_widget.setWindowFlags(Qt.Popup)
        self._calendar_widget.setGridVisible(True)
        self._calendar_widget.hide()
        self._calendar_widget.clicked.connect(self._on_date_selected)

        self.setLayout(root_layout)

    def _validate_date_input(self):
        if self._is_date_input_valid():
            self._date_field.setStyleSheet("")
        else:
            self._date_field.setStyleSheet("color: red;")

    def _is_date_input_valid(self):
        entered_text = self._date_field.text()

        if not entered_text:
            return True

        try:
            parsed_date = QDate.fromString(entered_text, "yyyy-MM-dd")
            return parsed_date.isValid()
        except ValueError:
            return False

    def _validate_time_input(self):
        if self.is_time_input_valid():
            self._time_field.setStyleSheet("")
        else:
            self._time_field.setStyleSheet("color: red;")

    def is_time_input_valid(self):
        entered_text = self._time_field.text()

        if not entered_text:
            return True

        try:
            parsed_time = QTime.fromString(entered_text, "hh:mm")
            return parsed_time.isValid()
        except ValueError:
            return False

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
