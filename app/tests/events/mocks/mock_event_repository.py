
from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository


class MockEventRepository(EventRepository):

    def __init__(self):
        self._events = []

    def save(self, event: Event):
        self._events.append(event)
        return event

    def markAsNotified(self, event: Event) -> None:
        pass

    def list(self):
        return self._events
