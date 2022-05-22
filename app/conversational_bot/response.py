from sso.domain.user import User


class Response:
    def __init__(self, user: User, text: str, intent, entities):
        self.user = user
        self.text = text
        self.intent = intent
        self.entities = entities

