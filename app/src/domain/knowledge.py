import json


class Knowledge:
    def __init__(self, text, domain, intent, entities, response):
        self.text = text
        self.domain = domain
        self.intent = intent
        self.entities = entities.replace("'", "@")
        self.response = response
