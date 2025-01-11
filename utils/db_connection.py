import os

from select import select
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



    def addNewDoctor(self, name, surname, login, password, organisation_id):
        new_doctor_data = {
            "name": name,
            "surname": surname,
            "login": login,
            "password": password,
            "role": "Dentist",
            "organization_id": organisation_id
        }

        try:
            response = self.client.table('users').insert(new_doctor_data).execute()
            print(response)
            return "Doctor added successfully!"
        except Exception as e:
            print(f"An error occurred while adding the doctor: {str(e)}")
            return f"An error occurred while adding the doctor: {str(e)}"


    def delete_doctor_by_id(self, doctor_id):
        try:
            response = self.client.table('users').delete().eq("login", doctor_id).execute()
            print(response)
            return "deleted"
        except Exception as e:
            print(f"error {str(e)}")
            return f"error {str(e)}"


    def search_doctors(self, name, surname):
        try:
            query = self.client.table('users') \
                .select("*") \
                .eq("role", "Dentist")\
                .neq("password", "NULL")

            if name:
                query = query.ilike("name", f"%{name}%")

            if surname:
                query = query.ilike("surname", f"%{surname}%")






            response = query.execute()


            for doctor in response.data:
               doctor["id"] = doctor.pop("user_id", doctor.get("id"))

            return response.data

        except Exception as e:
            print(f"An error occurred while retrieving doctors: {str(e)}")
            raise DBUnableToGetData()







    def update_doctor_password(self, doctor_id, hashed_password):
        try:
            response = self.client.table('users').update({"password": hashed_password}).eq("userid", doctor_id).execute()
            print(response)
        except Exception as e:
            print(f"Error updating doctor password: {str(e)}")
            raise

    def update_doctor_surname(self, doctor_id, new_surname):
        try:
            response = self.client.table('users').update({"surname": new_surname}).eq("userid", doctor_id).execute()
            print(response)
        except Exception as e:
            print(f"Error updating doctor surname: {str(e)}")
            raise

    def update_dotor_name(self, doctor_id, new_name):
        try:
            response = self.client.table('users').update({"name": new_name}).eq("userid", doctor_id).execute()
            print(response)
        except Exception as e:
            print(f"Error updating doctor name: {str(e)}")
            raise

    def update_doctor_login(self, doctor_id, new_login):
        try:
            response = self.client.table('users').update({"login": new_login}).eq("userid", doctor_id).execute()
            print(response)
        except Exception as e:
            print(f"Error updating doctor login: {str(e)}")
            raise