import uuid


class IntentTemplate:
    def generate(self, intent: str):
        return {"id": str(uuid.uuid4()), "name": intent}
