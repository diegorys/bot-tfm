import json


class Entry:
    def __init__(self, id: str, text: str, intent: str, entities):
        self.id = id
        self.text = text
        self.intent = intent
        self.entities = entities
