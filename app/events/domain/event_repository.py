from events.domain.event import Event


class EventRepository:
    def save(self, event: Event) -> None:
        pass

    def markAsNotified(self, event: Event) -> None:
        pass

    def getPendingEvents(self):
        pass
