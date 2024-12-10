import os
from supabase import create_client, Client
from dotenv import load_dotenv

from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.user_session import UserSession

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

            if patient_id :
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

