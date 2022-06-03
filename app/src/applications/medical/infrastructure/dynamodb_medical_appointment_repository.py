import os
import time
import boto3
from src.applications.medical.domain.medical_appointment import MedicalAppointment
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository


class DynamoDBMedicalAppointmentRepository(MedicationUserRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-medical-appointments")

    def save(self, medicalAppointment: MedicalAppointment):
        timestamp = str(time.time())
        response = self.table.put_item(
            Item={
                "id": str(timestamp),
                "user": medicalAppointment.user.username,
                "medication": medicalAppointment.speciality.name,
                "date": medicalAppointment.date.date,
                "createdAt": timestamp,
                "updatedAt": timestamp,
            }
        )
        print(response)
        return response
