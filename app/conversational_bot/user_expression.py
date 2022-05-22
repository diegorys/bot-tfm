from sso.domain.user import User


class UserExpression:
    def __init__(self, id, user: User, text, intent, entities, response: str, date=None):
        self.id = id
        self.user = user
        self.text = text
        self.intent = intent
        self.entities = entities
        self.response = response
        self.date = date
