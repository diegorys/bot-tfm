from decimal import Decimal
import os
import time
import boto3
from src.sso.domain.user import User
from src.events.domain.event_repository import EventRepository
from src.events.domain.event import Event


class DynamoDBEventRepository(EventRepository):
    def __init__(self):
        stage = os.environ["STAGE"]
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(f"tfm-{stage}-events")

    def save(self, event: Event) -> None:
        timestamp = str(time.time())
        item = {
            "id": event.id,
            "user": event.user.metadata["telegram_id"],
            "intent": event.intent,
            "entities": event.entities,
            "timestamp": Decimal(event.timestamp),
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }
        response = self.table.put_item(Item=item)
        if 200 != response["ResponseMetadata"]["HTTPStatusCode"]:
            raise Exception("Error saving event!")

    def markAsNotified(self, event: Event) -> None:
        response = self.table.delete_item(Key={"id": event.id})
        return response

    def list(self):
        response = self.table.scan()["Items"]
        print(response)
        events = []
        for item in response:
            user = User("", {"telegram_id": item["user"]})
            event = Event(
                user, item["intent"], item["entities"], float(item["timestamp"]), item["id"]
            )
            events.append(event)
        return events
