import os
import uuid
import time
import boto3
from boto3.dynamodb.conditions import Attr
from dialogs.domain.dialog_repository import DialogRepository

TABLE_NAME = os.environ["DIALOGS_TABLE"]

print(f"DIALOGS TABLE NAME!!!: {TABLE_NAME}")


class DynamoDBDialogRepository(DialogRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, dialog):
        exists = self.exists(dialog)
        if exists:
            raise Exception(f"Error at insert duplicated message")
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print("PUT ITEM")
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
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan()

        print(len(response["Items"]), TABLE_NAME)
        return response["Items"]

    def listDomain(self, domain):
        pass

    def listIntent(self, intent):
        pass

    def truncate(self):
        pass

    def exists(self, dialog):
        print(f"BUSCO {dialog.date} - {dialog.text}")
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(
            FilterExpression=Attr("date").eq(dialog.date) & Attr("text").eq(dialog.text)
        )

        print(len(response["Items"]))
        return len(response["Items"]) > 0
