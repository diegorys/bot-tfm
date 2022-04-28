import os
import uuid
import time
import boto3
from boto3.dynamodb.conditions import Attr

TABLE_NAME = os.environ["DATASET_TABLE"]

print(f"TABLE NAME!!!: {TABLE_NAME}")


class DynamoDBDatasetRepository:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def create(self, entry):
        exists = self.exists(entry)
        if exists:
            raise Exception(f"Error at insert duplicated dataset entry")
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print("PUT ITEM")
        entry.id = str(uuid.uuid4())
        response = table.put_item(
            Item={
                "id": entry.id,
                "text": entry.text,
                "intent": entry.intent,
                "entities": entry.entities,
                "createdAt": timestamp,
                "updatedAt": timestamp,
            }
        )
        print(response)
        return response

    def update(self, entry):
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print("PUT ITEM")
        entry.id = str(uuid.uuid4())
        response = table.put_item(
            Item={
                "id": entry.id,
                "text": entry.text,
                "intent": entry.intent,
                "entities": entry.entities,
                "createdAt": timestamp,
                "updatedAt": timestamp,
            }
        )
        print(response)
        return response

    def list(self):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan()

        print(len(response["Items"]))
        return response["Items"]

    def listDomain(self, domain):
        pass

    def listIntent(self, intent):
        pass

    def truncate(self):
        pass

    def exists(self, entry):
        print(f"BUSCO {entry.text}")
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(
            FilterExpression=Attr("text").eq(entry.text)
        )

        print(len(response["Items"]))
        return len(response["Items"]) > 0
