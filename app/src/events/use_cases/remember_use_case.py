from datetime import datetime, timedelta
from src.sso.domain.user import User
from src.conversational_bot.client import Client
from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository


class RememberUseCase:
    def __init__(self, repository: EventRepository, client: Client):
        self.repository = repository
        self.client = client

    def execute(self, nextTick: str):
        events = self.repository.getPendingEvents(nextTick)
        for event in events:
            user = User("", {"telegram_id": event.user})
            text = self.formatResponse(event)
            self.client.emit(user, text)
            self.repository.markAsNotified(event)

    def formatResponse(self, event: Event):
        timestamp = datetime.fromtimestamp(event.timestamp)
        localeDate = timestamp + timedelta(hours=2)
        date = localeDate.strftime("%H:%M")

        text = f"{event.intent}, {date}: "
        for entityName in event.entities.keys():
            text += f"{entityName} {event.entities[entityName]} "
        text = text.strip()
        return text
