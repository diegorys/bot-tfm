import os
import time
import boto3
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository


class DynamoDBMedicationUserRepository(MedicationUserRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-medication-user")

    def save(self, medicationUser: MedicationUser):
        timestamp = str(time.time())
        response = self.table.put_item(
            Item={
                "id": str(timestamp),
                "user": medicationUser.user.username,
                "medication": medicationUser.medication.name,
                "date": medicationUser.date.date,
                "createdAt": timestamp,
                "updatedAt": timestamp
            }
        )
        print(response)
        return response
