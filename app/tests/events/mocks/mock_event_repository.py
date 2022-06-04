
from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository


class MockEventRepository(EventRepository):
    def save(self, event: Event):
        return event

    def markAsNotified(self, event: Event) -> None:
        pass

    def getPendingEvents(self, nextTick: str):
        pass
