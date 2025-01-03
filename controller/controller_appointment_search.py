from PySide6.QtWidgets import QTableWidgetItem


class AppointmentSearchController:

    def __init__(self, view):
        self.view = view


    def search_appointments(self):
        """
        Fetch and display appointments based on search criteria.
        """
        # Collect search criteria from the form
        patient_name = self.view.name_field.text().strip()
        patient_surname = self.view.surname_field.text().strip()

        # Check if date range is left unspecified
        date_from = self.view.date_from_field.date().toString("yyyy-MM-dd") if self.view.date_from_field.text() else None
        date_to = self.view.date_to_field.date().toString("yyyy-MM-dd") if self.view.date_to_field.text() else None

        # Check if time range is left unspecified
        time_from = self.view.time_from_field.time().toString("HH:mm:ss") if self.view.time_from_field.text() else "00:00:00"
        time_to = self.view.time_to_field.time().toString("HH:mm:ss") if self.view.time_to_field.text() else "23:59:59"

        type_of_visit = self.view.type_field.text().strip()

        # Call the database function (replace this with your actual database query)
        appointments = self.fetch_appointments(
            patient_name, patient_surname, date_from, date_to, type_of_visit, time_from, time_to
        )

        # Update the table with the results
        self.view.table.setRowCount(0)  # Clear previous contents
        for appointment in appointments:
            row_position = self.view.table.rowCount()
            self.view.table.insertRow(row_position)
            self.view.table.setItem(row_position, 0, QTableWidgetItem(str(appointment.get('id', 'N/A'))))
            self.view.table.setItem(row_position, 1, QTableWidgetItem(appointment.get('patient_name', 'N/A')))
            self.view.table.setItem(row_position, 2, QTableWidgetItem(appointment.get('patient_surname', 'N/A')))
            self.view.table.setItem(row_position, 3, QTableWidgetItem(appointment.get('date', 'N/A')))
            self.view.table.setItem(row_position, 4, QTableWidgetItem(appointment.get('time', 'N/A')))
            self.view.table.setItem(row_position, 5, QTableWidgetItem(appointment.get('type', 'N/A')))
            self.view.table.setItem(row_position, 6, QTableWidgetItem(appointment.get('notes', 'N/A')))

    def fetch_appointments(self, patient_name, patient_surname, date_from, date_to, type_of_visit, time_from, time_to):
        """
        Simulates fetching appointments from the database. Replace this with actual DB logic.
        """
        # Sample data for demonstration purposes
        sample_appointments = [
            {
                "id": 1,
                "patient_name": "John",
                "patient_surname": "Doe",
                "date": "2024-12-25",
                "time": "10:00:00",
                "type": "Consultation",
                "notes": "Routine check-up",
            },
            {
                "id": 2,
                "patient_name": "Jane",
                "patient_surname": "Smith",
                "date": "2024-12-26",
                "time": "11:00:00",
                "type": "Procedure",
                "notes": "Tooth extraction",
            },
        ]

        # Apply filtering (replace this logic with real database queries)
        return [
            appointment for appointment in sample_appointments
            if (not patient_name or patient_name.lower() in appointment['patient_name'].lower())
            and (not patient_surname or patient_surname.lower() in appointment['patient_surname'].lower())
            and (not date_from or appointment['date'] >= date_from)
            and (not date_to or appointment['date'] <= date_to)
            and (not type_of_visit or type_of_visit.lower() in appointment['type'].lower())
            and (not time_from or appointment['time'] >= time_from)
            and (not time_to or appointment['time'] <= time_to)
        ]
