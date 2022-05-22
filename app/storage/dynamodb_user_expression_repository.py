import os
import time
import boto3
from boto3.dynamodb.conditions import Attr
from conversational_bot.user_expression import UserExpression
from conversational_bot.user_expression_repository import UserExpressionRepository

TABLE_NAME = os.environ["DIALOGS_TABLE"]


class DynamoDBUserExpressionRepository(UserExpressionRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, userExpression: UserExpression):
        exists = self._exists(userExpression)
        if exists:
            raise Exception(f"Error at insert duplicated message")
        table = self.dynamodb.Table(TABLE_NAME)
        timestamp = str(time.time())
        print("PUT ITEM")
        response = table.put_item(
            Item={
                "id": str(userExpression.id),
                "date": str(userExpression.date),
                "user": {
                    "name": userExpression.user.username,
                    "metadata": userExpression.user.metadata,
                },
                "text": userExpression.text,
                "intent": userExpression.intent,
                "entities": userExpression.entities,
                "response": userExpression.response,
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

    def _exists(self, dialog):
        print(f"BUSCO {dialog.date} - {dialog.text}")
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(
            FilterExpression=Attr("date").eq(dialog.date) & Attr("text").eq(dialog.text)
        )

        print(len(response["Items"]))
        return len(response["Items"]) > 0
