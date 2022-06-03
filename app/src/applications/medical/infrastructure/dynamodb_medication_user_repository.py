import os
import uuid
import time
import boto3
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository


class DynamoDBMedicationUserRepository(MedicationUserRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-medication-user")


    def save(self, medicationuser: MedicationUser):
        timestamp = str(time.time())
        response = self.table.put_item(
            Item={
                "id": str(timestamp),
                "user": medicationuser.user.username,
                "medication": medicationuser.medication.name,
                "date": medicationuser.date.date,
                "createdAt": timestamp,
                "updatedAt": timestamp
            }
        )
        stage = os.environ["STAGE"]
        print(f"tfm-{stage}-medication-user")
        print(response)
        return response
