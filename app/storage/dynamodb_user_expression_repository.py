import os
import time
import boto3
import json
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
        print(userExpression.id)
        print(str(userExpression.date))
        print(userExpression.user.username)
        print(userExpression.user.metadata)
        print(userExpression.text)
        print(userExpression.intent)
        print(userExpression.entities)
        print(userExpression.response)
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
        print("DONE")
        print(response)
        return response

    def list(self):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan()

        print(len(response["Items"]), TABLE_NAME)
        return response["Items"]

    def _exists(self, userExpression: UserExpression):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan(
            FilterExpression=Attr("date").eq(userExpression.date)
            & Attr("text").eq(userExpression.text)
        )
        return len(response["Items"]) > 0
