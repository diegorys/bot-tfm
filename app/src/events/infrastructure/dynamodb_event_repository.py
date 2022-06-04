import os
import time
import boto3
from src.events.domain.event import Event


class DynamoDBEventRepository:
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
            "date": event.date,
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }
        response = self.table.put_item(Item=item)
        return response

    def markAsNotified(self, event: Event) -> None:
        response = self.table.delete_item(
            Key={"id": event.id}
        )
        return response

    def getPendingEvents(self):
        pass
