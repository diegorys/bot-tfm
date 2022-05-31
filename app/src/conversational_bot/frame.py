from src.sso.domain.user import User


class Frame:
    def __init__(self, intent: str, user: User, originalText: str, entities={}):
        self.intent = intent
        self.user: User = user
        self.originalText = originalText
        self.entities = entities

    def addEntity(self, entity: str, value) -> None:
        self.entities[entity] = value

    def generate(self, template: str) -> str:
        text = template
        for entity in self.entities.keys():
            value = self.entities[entity]
            text = text.replace(f"[{entity}]", value)
        return text

    def isComplete(self) -> bool:
        for entity in self.entities.keys():
            value = self.entities[entity]
            if not value:
                return False
        return True
