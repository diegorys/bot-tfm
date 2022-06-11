from abc import abstractmethod
from datetime import datetime, timedelta
from src.events.domain.event import Event


class EventRepository:
    @abstractmethod
    def save(self, event: Event) -> None:
        pass

    @abstractmethod
    def markAsNotified(self, event: Event) -> None:
        pass

    def getPendingEvents(self, delta: int):
        timestamp = (datetime.now() + timedelta(minutes=delta) + timedelta(hours=2)).timestamp()
        allEvents = self.list()
        print(f"Eventos: {len(allEvents)}")
        events = []
        for event in allEvents:
            if event.hasExpired(timestamp):
                events.append(event)
        return events

    @abstractmethod
    def list(self):
        pass
