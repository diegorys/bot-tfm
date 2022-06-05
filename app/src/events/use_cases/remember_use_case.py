from datetime import datetime, timedelta
from src.sso.domain.user import User
from src.conversational_bot.client import Client
from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository


class RememberUseCase:
    def __init__(self, repository: EventRepository, client: Client):
        self.repository = repository
        self.client = client

    def execute(self, delta: int):
        print(f"Get pending events for delta {delta}")
        events = self.repository.getPendingEvents(delta)
        print(f"Pending events: {len(events)}")
        for event in events:
            text = self.formatResponse(event)
            print(f"Response: {text}")
            self.client.emit(event.user, text)
            self.repository.markAsNotified(event)
            print(f"Done event {text}")
        print("done all")

    def formatResponse(self, event: Event):
        timestamp = datetime.fromtimestamp(event.timestamp)
        localeDate = timestamp
        date = localeDate.strftime("%H:%M")

        text = f"{event.intent}, {date}: "
        for entityName in event.entities.keys():
            text += f"{entityName} {event.entities[entityName]} "
        text = text.strip()
        return text
