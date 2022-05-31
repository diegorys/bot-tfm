import os
import uuid
import time
import boto3
from src.applications.medical.domain.medication import Medication
from src.applications.medical.domain.medication_repository import MedicationRepository

TABLE_NAME = os.environ["MEDICINES_TABLE"]

class DynamoDBMedicationRepository(MedicationRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, dialog):
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print('PUT ITEM')
        response = table.put_item(
            Item={
                "id": str(dialog.id),
                "date": str(dialog.date),
                "user": {"id": dialog.userid, "name": dialog.username},
                "text": dialog.text,
                "domain": dialog.domain,
                "intent": dialog.intent,
                "entities": dialog.entities,
                "response": dialog.response,
                "createdAt": timestamp,
                "updatedAt": timestamp,
            }
        )
        print(response)
        return response

    def list(self):
        pass

    def listDomain(self, domain):
        pass

    def listIntent(self, intent):
        pass

    def truncate(self):
        pass
