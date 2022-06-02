from src.sso.domain.user import User


class Event:
    def __init__(self, user: User, intent: str, entities, date):
        self.user = user
        self.intent = intent
        self.entities = entities
        self.date = date

    def hasToBeNotified(self):
        # TODO if self.date < now
        pass
