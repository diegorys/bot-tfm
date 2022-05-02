import os
import uuid
import time
import boto3
from boto3.dynamodb.conditions import Attr

from sso.domain.user import User
from sso.domain.user_repository import UserRepository

TABLE_NAME = os.environ["USERS_TABLE"]


class DynamoDBUsersRepository(UserRepository):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def save(self, user: User):
        return user

    def list(self):
        users = []
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.scan()
        items = response["Items"]
        for item in items:
            users.append(
                User(
                    item["name"],
                    {
                        "telegram_id": item["telegram_id"],
                        "username": item["name"],
                        "caregiver": item["caregiver"],
                        "dependents": item["dependents"],
                    },
                )
            )
        return users
