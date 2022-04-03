class Response:
    def __init__(self, user, text):
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