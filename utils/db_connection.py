import base64
import os
from typing import Optional

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

    def get_appointment_details(self, organization_id: int, appointment_id: int):
        try:
            response = self.client.rpc('get_appointment_details', {
                'organization_id_input': organization_id,
                'appointment_id_input': appointment_id
            }).execute()
            return response.data
        except Exception as e:
            print(f"An error occurred while retrieving the appointment details: {str(e)}")
            raise DBUnableToGetData()

    def is_appointment_exsist(self, organization_id: int, appointment_id: int):
        try:
            response = self.client.rpc('is_appointment_exist_by_id', {
                'organization_id_input': organization_id,
                'appointment_id_input': appointment_id
            }).execute()
            return response.data
        except Exception as e:
            print(f"An error occurred while retrieving the appointment: {str(e)}")
            raise DBUnableToGetData()

    def alter_appointment_dental_diagram(self, appointment_id, dental_diagram):
        try:
            dental_diagram_encoded = base64.b64encode(dental_diagram).decode("utf-8")

            response = self.client.table("appointments_details") \
                .update({
                "dental_diagram": dental_diagram_encoded
            }) \
                .eq("appointment_id", appointment_id) \
                .execute()

            return response.data
        except Exception as e:
            print(f"An error occurred while updating the appointment: {str(e)}")
            raise DBUnableToGetData()

    def alter_appointment_details_using_id(self, appointment_id: int, services: Optional[str],
                                           symptoms_description: Optional[str],
                                           mucous_membrane: Optional[str], periodontium: Optional[str],
                                           hygiene: Optional[str],
                                           oral_additional_info: Optional[str], dental_diagram: Optional[bytes],
                                           additional_info: Optional[str],
                                           medications: Optional[str]):
        try:
            dental_diagram_encoded = base64.b64encode(dental_diagram).decode("utf-8")
            updates = {
                "services": services,
                "symptoms_description": symptoms_description,
                "mucous_membrane": mucous_membrane,
                "periodontium": periodontium,
                "hygiene": hygiene,
                "oral_additional_info": oral_additional_info,
                "dental_diagram": dental_diagram_encoded,
                "additional_info": additional_info,
                "medications": medications
            }
            response = self.client.table("appointments_details").update(updates).eq("appointment_id",
                                                                                    appointment_id).execute()
            return response
        except Exception as e:
            print(f"An error occurred while updating the appointment: {str(e)}")
            raise DBUnableToGetData()

    def insert_appointment_details(self, appointment_id: int, services: Optional[str],
                                   symptoms_description: Optional[str], mucous_membrane: Optional[str],
                                   periodontium: Optional[str], hygiene: Optional[str],
                                   oral_additional_info: Optional[str], dental_diagram: Optional[bytes],
                                   additional_info: Optional[str], medications: Optional[str]):
        try:
            dental_diagram_encoded = (
                base64.b64encode(dental_diagram).decode("utf-8") if dental_diagram else None
            )

            new_record = {
                "appointment_id": appointment_id,
                "services": services,
                "symptoms_description": symptoms_description,
                "mucous_membrane": mucous_membrane,
                "periodontium": periodontium,
                "hygiene": hygiene,
                "oral_additional_info": oral_additional_info,
                "dental_diagram": dental_diagram_encoded,
                "additional_info": additional_info,
                "medications": medications
            }

            response = self.client.table("appointments_details").insert(new_record).execute()

            return response
        except Exception as e:
            print(f"An error occurred while inserting the appointment: {str(e)}")
            # TO-DO Change exceptions
            raise DBUnableToGetData()
