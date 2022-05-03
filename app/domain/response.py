from sso.domain.user import User


class Response:
    def __init__(self, user: User, text):
        self.user = user
        self.text = text
        self.domain = ""
        self.intent = ""
        self.probability = 0
        self.command = ""

    def setDomain(self, domain):
        self.domain = domain

    def setIntent(self, intent):
        self.intent = intent

    def setProbability(self, probability):
        self.probability = probability

    def setCommand(self, command):
        self.command = command