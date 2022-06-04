import time
from src.sso.domain.user import User


class Event:
    def __init__(self, user: User, intent: str, entities, date: str):
        timestamp = str(time.time())
        self.id = str(timestamp)
        self.user = user
        self.intent = intent
        self.entities = entities
        self.date = date
