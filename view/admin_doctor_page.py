# view/admin_doctor_page.py

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QFormLayout, QFrame, QWidget, QApplication, QCheckBox, QMessageBox
)
from PySide6.QtCore import Qt, QEvent
import sys

class AdminDoctorPage(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen

        self.setWindowTitle("Doctor Admin Page")
        from controller.admin_doctor_controller import DoctorController  # Local import to avoid circular import
        self.controller = DoctorController(self)


        self.main_layout = QHBoxLayout()

        # Left
        self.form_layout = QFormLayout()

        self.name_field = QLineEdit()
        self.form_layout.addRow("Name", self.name_field)

        self.surname_field = QLineEdit()
        self.form_layout.addRow("Surname", self.surname_field)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.controller.search_doctors)
        self.form_layout.addRow(self.search_button)

        self.left_layout = QVBoxLayout()
        self.left_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.left_layout, stretch=1)

        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.vertical_line)

        # Right Layout
        self.right_layout = QVBoxLayout()

        self.add_doctor_button = QPushButton("Add Doctor")
        self.add_doctor_button.setStyleSheet("background-color: green; color: white;")
        self.add_doctor_button.clicked.connect(self.controller.add_doctor_form)
        self.right_layout.addWidget(self.add_doctor_button, alignment=Qt.AlignTop | Qt.AlignRight)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([ "Name", "Surname", "Login", "Password", "Select"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.right_layout.addWidget(self.table)

        self.edit_doctor_button = QPushButton("Edit Doctor")
        self.edit_doctor_button.setStyleSheet("background-color: blue; color: white;")
        self.right_layout.addWidget(self.edit_doctor_button, alignment=Qt.AlignBottom | Qt.AlignRight)

        self.delete_doctor_button = QPushButton("Delete Doctor")
        self.delete_doctor_button.setStyleSheet("background-color: red; color: white;")
        self.right_layout.addWidget(self.delete_doctor_button, alignment=Qt.AlignBottom | Qt.AlignRight)
        self.delete_doctor_button.clicked.connect(self.delete_selected_doctors)

        self.main_layout.addLayout(self.right_layout, stretch=3)  # Larger stretch factor for the right side

        self.setLayout(self.main_layout)

        self.search_button.installEventFilter(self)
        self.add_doctor_button.installEventFilter(self)
        self.delete_doctor_button.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            if source == self.search_button:
                source.setStyleSheet("background-color: #A9A9A9; color: white;")
            elif source == self.add_doctor_button:
                source.setStyleSheet("background-color: #006400; color: white;")
            elif source == self.delete_doctor_button:
                source.setStyleSheet("background-color: #8B0000; color: white;")
        elif event.type() == QEvent.Leave:
            if source == self.search_button:
                source.setStyleSheet("background-color: #C0C0C0;")
            elif source == self.add_doctor_button:
                source.setStyleSheet("background-color: green; color: white;")
            elif source == self.delete_doctor_button:
                source.setStyleSheet("background-color: red; color: white;")
        return super().eventFilter(source, event)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)



    def populate_table(self, doctors):
        self.table.setRowCount(len(doctors))
        for row, doctor in enumerate(doctors):
            self.table.setItem(row, 0, QTableWidgetItem(doctor["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(doctor["surname"]))
            self.table.setItem(row, 2, QTableWidgetItem(doctor["login"]))
            self.table.setItem(row, 3, QTableWidgetItem(doctor["password"]))
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.handle_checkbox_state_change)

            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)

            self.table.setCellWidget(row, 4, widget)




    def handle_checkbox_state_change(self, state):
        checkbox = self.sender()
        doctor_id = checkbox.doctor_id
        if state == Qt.Checked:
            print(f"Doctor {doctor_id} selected")
        else:
            print(f"Doctor {doctor_id} deselected")

    def delete_selected_doctors(self):
        selected_doctor_ids = []
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 6)
            if checkbox and checkbox.isChecked():
                selected_doctor_ids.append(checkbox.doctor_id)
        if selected_doctor_ids:
            self.controller.delete_selected_doctors(selected_doctor_ids)
        else:
            self.show_error("No doctors selected for deletion.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminDoctorPage(None)
    window.show()
    sys.exit(app.exec())