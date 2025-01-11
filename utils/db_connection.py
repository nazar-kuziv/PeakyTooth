import os
from datetime import datetime

from dotenv import load_dotenv
from supabase import create_client, Client

from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData

load_dotenv()


class DBConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DBConnection(metaclass=DBConnectionMeta):
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        try:
            self.client: Client = create_client(url, key)
        except:
            raise DBUnableToConnect()

    def get_user(self, login: str):
        try:
            return self.client.table("users").select("*, organizations(*)").eq("login", login).execute()
        except:
            raise DBUnableToGetData()

    def addNewPatient(self, name, surname, date_of_birth, sex, email, telephone, analgesics_allergy, organisation_id):
        new_patient_data = {
            "patient_name": name,
            "patient_surname": surname,
            "date_of_birth": date_of_birth,
            "sex": sex,
            "email": email,
            "telephone": telephone,
            "analgesics_allergy": analgesics_allergy,
            "organization_id": organisation_id
        }

        try:
            response = self.client.table('patients').insert(new_patient_data).execute()
            print(response)
            return "Patient added successfully!"
        except Exception as e:
            print(f"An error occurred while adding the patient: {str(e)}")
            return f"An error occurred while adding the patient: {str(e)}"

    def find_patients(self, patient_id, name, surname, organization_id):
        try:
            query = self.client.table('patients') \
                .select("*") \
                .eq("organization_id", organization_id)

            if patient_id:
                query = query.eq("id", patient_id)
            if name:
                query = query.eq("patient_name", name)
            if surname:
                query = query.eq("patient_surname", surname)

            response = query.execute()

            return response.data

        except Exception as e:
            print(f"An error occurred while retrieving patients: {str(e)}")
            raise DBUnableToGetData()

    def alter_patient_data(self, doctor_organization_id, patient_id, name, surname, date_of_birth, analegisics_allergy,
                           telephone, email):
        try:
            response = self.client.table("patients") \
                .update({
                "patient_name": name,
                "patient_surname": surname,
                "date_of_birth": date_of_birth,
                "analgesics_allergy": analegisics_allergy,
                "telephone": telephone,
                "email": email
            }) \
                .eq("id", patient_id) \
                .eq("organization_id", doctor_organization_id) \
                .execute()

            return response.data
        except Exception as e:
            print(f"An error occurred while updating the patient: {str(e)}")
            raise DBUnableToGetData()

    def get_patient(self, organization_id, patient_id):
        try:
            response = self.client.table("patients") \
                .select("*") \
                .eq("organization_id", organization_id) \
                .eq("id", patient_id) \
                .execute()

            return response.data
        except Exception as e:
            print(f"An error occurred while retrieving the patient: {str(e)}")
            raise DBUnableToGetData()

    def create_appointment(self, appointment_data):
        try:
            self.client.table("appointments").insert(appointment_data).execute()
            return "Appointment created successfully!"
        except Exception as e:
            print(f"An error occurred while adding the appointment: {str(e)}")
            raise DBUnableToConnect()

    def get_appointments_by_date(self, dentist_id, date):
        try:
            # Start query for appointments table
            query = (
                self.client.table('appointments')
                .select(
                    'id, date, time, dentist_id, type, notes, '
                    'patients(patient_name, patient_surname)'  # Fetch related fields from patients
                )
            )

            query = query.eq('dentist_id', dentist_id)

            query = query.eq('date', date)

            query = query.order('time, date')

            response = query.execute()
            return response
        except Exception as e:
            print ("An error occurred while retrieving the appointments: " + str(e))
            raise DBUnableToGetData()

    def get_appointment_by_id(self, appointment_id):
        try:
            # Correct the foreign key relationship and specify the appropriate fields
            query = (
                self.client
                .table("appointments")
                .select('id, date, time, dentist_id, type, notes, patient_id, '
                        'patients(id, patient_name, patient_surname)')
                .eq('id', appointment_id)
            )
            response = query.execute()

            return response

        except Exception as e:
            print("An error occurred while retrieving the appointments: " + str(e))
            raise DBUnableToGetData()

    def get_appointments_with_filter(self, dentist_id, name, surname, date_from, date_to, time_from, time_to, visit_type):
        try:
            # Begin constructing the query
            query = self.client.table('appointments').select(
                'id, date, time, type, patients(*)'
            )
            query = query.eq('dentist_id', dentist_id)

#            if name:
 #               query = query.eq('patients.patient_name', name)
   #         if surname:
  #              query = query.eq('patients.patient_surname', surname)


            if date_from and not date_to:
                query = query.gte('date', date_from)
            elif date_to and not date_from:
                query = query.lte('date', date_to)
            elif date_from and date_to:
                query = query.gte('date', date_from).lte('date', date_to)

            if time_from and not time_to:
                query = query.gte('time', time_from)
            elif time_to and not time_from:
                query = query.lte('time', time_to)
            elif time_from and time_to:
                query = query.gte('time', time_from).lte('time', time_to)
            if visit_type:
                query = query.eq('type', visit_type)

            # Sort the results by date and time
            query = query.order('date, time')

            # Execute the query
            response = query.execute().data

            filtered = [
                appointment for appointment in response
                if (name is None or appointment['patients']['patient_name'] == name) and
                   (surname is None or appointment['patients']['patient_surname'] == surname)
            ]

            return filtered

        except Exception as e:
            print(f"An error occurred while searching for appointments: {str(e)}")
            raise DBUnableToGetData()

    def update_appointment(self, appointment_id, date, time, appointment_type, notes):
        try:
            # Prepare the new data for updating
            update_data = {
                "date": date,
                "time": time,
                "type": appointment_type,
                "notes": notes
            }

            # Start the update query
            response = self.client.table("appointments") \
                .update(update_data) \
                .eq("id", appointment_id)  # Specify the appointment to be updated

            # Execute the query and return the result
            response.execute()

            return "Appointment was updated successfully!"

        except Exception as e:
            print(f"An error occurred while updating the appointment: {str(e)}")
            raise DBUnableToGetData()
