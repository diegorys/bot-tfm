import os
import boto3

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
            user = User(
                item["name"], {"telegram_id": item["telegram_id"], "username": item["name"]}
            )
            if "caregiver" in item.keys():
                user.metadata["caregiver"] = item["caregiver"]
            if "dependents" in item.keys():
                user.metadata["dependents"] = item["dependents"]
            users.append(user)
        return users
