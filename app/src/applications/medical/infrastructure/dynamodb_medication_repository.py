import os
import uuid
import time
import boto3
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository

TABLE_NAME = os.environ["MEDICATION_USER_TABLE"]

class DynamoDBMedicationRepository(MedicationUserRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, medicationuser: MedicationUser):
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print('PUT ITEM')
        response = table.put_item(
            Item={
                # "id": str(dialog.id),
                # "date": str(dialog.date),
                # "user": {"id": dialog.userid, "name": dialog.username},
                # "text": dialog.text,
                # "domain": dialog.domain,
                # "intent": dialog.intent,
                # "entities": dialog.entities,
                # "response": dialog.response,
                # "createdAt": timestamp,
                # "updatedAt": timestamp,
            }
        )
        print(response)
        return response
        