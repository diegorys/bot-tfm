from sso.domain.user import User


class Frame:
    def __init__(self, intent, user: User, originalText, entities={}):
        self.intent = intent
        self.user: User = user
        self.originalText = originalText
        self.entities = entities
