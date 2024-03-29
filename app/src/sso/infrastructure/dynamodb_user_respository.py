import os
import time
from uuid import uuid4
import boto3
from src.sso.infrastructure.dynamodb_user_factory import DynamoDBUserFactory
from src.sso.domain.user import User
from src.sso.domain.user_repository import UserRepository


class DynamoDBUsersRepository(UserRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-users")

    def save(self, user: User):
        user.clearDependentsMetadata()
        timestamp = str(time.time())
        createdAt = None
        if user.id is None:
            user.id = str(uuid4())
            createdAt = timestamp
        item = {"id": user.id, "name": user.username}
        if createdAt is not None:
            item["createdAt"] = createdAt
        for key in user.metadata.keys():
            item[key] = user.metadata[key]
        item["updatedAt"] = timestamp
        print('SAVE ITEM')
        print(item)
        print("---------")
        response = self.table.put_item(Item=item)
        if 200 != response["ResponseMetadata"]["HTTPStatusCode"]:
            raise Exception("Error saving event!")

    def list(self):
        users = []
        userDict = {}
        response = self.table.scan()
        items = response["Items"]
        for item in items:
            user = DynamoDBUserFactory.create(item)
            users.append(user)
            userDict[user.id] = user
        for user in users:
            self.addRelations(userDict, user)
        return users
