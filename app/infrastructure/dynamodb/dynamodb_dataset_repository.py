import os
import uuid
import time
import boto3
from boto3.dynamodb.conditions import Attr
from dataset.domain.dataset_repository import DatasetRepository
from dataset.domain.entry import Entry

TABLE_NAME = os.environ["DATASET_TABLE"]


class DynamoDBDatasetRepository(DatasetRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def create(self, entry: Entry):
        exists = self.exists(entry)
        if exists:
            raise Exception(f"Error at insert duplicated dataset entry")
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
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
        return entry

    def update(self, entry: Entry):
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
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
        return response

    def list(self):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan()

        print(response["Items"])
        return response["Items"]

    def truncate(self):
        pass

    def exists(self, entry):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(FilterExpression=Attr("text").eq(entry.text))
        return len(response["Items"]) > 0

    def getByText(self, text):
        secureText = text.replace("'","\'")
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(FilterExpression=Attr("text").eq(secureText))
        if len(response["Items"]) > 0:
            item = response["Items"][0]
            entry = Entry(item["id"], item["text"], item["intent"], item["entities"])
            return entry
        return None
