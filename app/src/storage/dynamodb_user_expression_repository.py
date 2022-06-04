import os
import time
import boto3
import json
from boto3.dynamodb.conditions import Attr
from src.conversational_bot.user_expression import UserExpression
from src.conversational_bot.user_expression_repository import UserExpressionRepository


class DynamoDBUserExpressionRepository(UserExpressionRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-dialogs")

    def save(self, userExpression: UserExpression):
        exists = self._exists(userExpression)
        if exists:
            raise Exception(f"Error at insert duplicated message")
        timestamp = str(time.time())
        response = self.table.put_item(
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
        return response

    def list(self):
        response = self.table.scan()
        return response["Items"]

    def _exists(self, userExpression: UserExpression):
        response = self.table.scan(
            FilterExpression=Attr("date").eq(userExpression.date)
            & Attr("text").eq(userExpression.text)
        )
        return len(response["Items"]) > 0
