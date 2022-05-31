from src.events.domain.event import Event


class DynamoDBEventRepository:
    def save(self, event: Event) -> None:
        pass

    def markAsNotified(self, event: Event) -> None:
        pass

    def getPendingEvents(self):
        pass
