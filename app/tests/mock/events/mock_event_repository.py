from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository


class MockEventRepository(EventRepository):
    def save(self, event: Event):
        return event
