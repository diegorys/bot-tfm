from sso.domain.user import User


class Event:
    def __init__(self, name: str, user: User, entities, date):
        self.name = name
        self.user = user
        self.entities = entities
        self.date = date
    
    def hasToBeNotified(self):
        # TODO if self.date < now
        pass
