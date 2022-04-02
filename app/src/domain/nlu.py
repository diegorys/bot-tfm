class NLU:
    def __init__(self):
        self.domains = {}

    def handle(self, action):
        self.domains[action.command] = action

    def executeCommand(self, user, command):
        action = self.domains[command]
        return action.execute(user, command)

    def getResponse(self, user, text):
        domain, p = self.identifyDomain(text)
        domains = list(self.domains.keys())
        if domain not in domains:
            domain = domains[0]
        action = self.domains[domain]
        return domain, p, action.execute(user, text)

    def identifyDomain(self, text):
        pass

    def identifyEmotion(self, user, text):
        pass

    def getIntent(self, domain, text):
        pass

    def extractEntities(self, domain, intent, text):
        pass
