import os
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
        return user

    def list(self):
        users = []
        response = self.table.scan()
        items = response["Items"]
        for item in items:
            user = DynamoDBUserFactory.create(item)
            users.append(user)
        return users

    def getByMetadata(self, key, value):
        users = self.list()
        userDict = {}
        for user in users:
            userDict[user.id] = user
        foundUser = None
        for user in users:
            if str(value) == user.metadata[key]:
                foundUser = user
        if foundUser is None:
            raise Exception(f"User with metadata {key} - {value} not found")
        if "caregiver" in list(foundUser.metadata.keys()):
            foundUser.relations["caregiver"] = userDict[foundUser.metadata["caregiver"]]
        if "dependents" in list(foundUser.metadata.keys()):
            foundUser.relations["dependents"] = []
            for dependent in list(foundUser.metadata["dependents"]):
                foundUser.relations["dependents"].append(userDict[str(dependent)])
        return foundUser
