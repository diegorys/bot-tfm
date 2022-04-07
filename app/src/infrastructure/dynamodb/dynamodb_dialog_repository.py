import boto3
from domain.dialog import Dialog
from domain.dialog_repository import DialogRepository


class DynamoDBDialogRepository(DialogRepository):
    def __init__(self, name):
        self.name = name
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, dialog):
        table = self.dynamodb.Table("tfm-test-dialogs")
        response = table.put_item(
            Item={
                "date": dialog.date,
                "user": {"id": dialog.userid, "name": dialog.username},
                "text": dialog.text,
                "domain": dialog.domain,
                "intent": dialog.intent,
                "entities": dialog.entities,
                "response": dialog.response,
            }
        )
        return response

    def list(self):
        pass

    def listDomain(self, domain):
        pass

    def listIntent(self, intent):
        pass

    def truncate(self):
        pass
