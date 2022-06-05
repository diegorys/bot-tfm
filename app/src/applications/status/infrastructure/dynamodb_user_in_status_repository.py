import os
import time
import boto3
from decimal import Decimal
from src.applications.status.domain.status import Status
from src.sso.domain.user import User
from src.applications.status.domain.user_in_status import UserInStatus
from src.applications.status.domain.user_in_status_repository import UserInStatusRepository


class DynamoDBUserInStatusRepository(UserInStatusRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-status")

    def save(self, userInStatus: UserInStatus):
        timestamp = str(time.time())
        item = {
            "id": timestamp,
            "user": userInStatus.user.metadata["telegram_id"],
            "status": userInStatus.status.name,
            "timestamp": Decimal(userInStatus.timestamp),
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }
        response = self.table.put_item(Item=item)
        if 200 != response["ResponseMetadata"]["HTTPStatusCode"]:
            raise Exception("Error saving event!")

    def getStatusOf(self, user: User):
        id = user.metadata["telegram_id"]
        response = self.table.scan()["Items"]
        foundUserInStatus = None
        currentTimestamp = 0
        for item in response:
            checkTimestamp = float(item["timestamp"])
            if item["user"] == id and checkTimestamp > currentTimestamp:
                currentTimestamp = checkTimestamp
                status = Status(item["status"])
                foundUserInStatus = UserInStatus(user, status, currentTimestamp)

        if foundUserInStatus is None:
            raise Exception(f"User {id} not found")
        return foundUserInStatus
