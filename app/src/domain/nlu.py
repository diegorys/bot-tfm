class NLU:
    def __init__(self, knowledgeRepository):
        self.intents = {}
        self.knowledgeRepository = knowledgeRepository

    def handle(self, action):
        self.intents[action.command] = action

    def executeCommand(self, user, command):
        action = self.intents[command]
        return action.execute(user, command)

    def getResponse(self, user, text):
        domain, p = self.identifyDomain(text)
        print(f"Dominio {domain}")
        intent, p = self.identifyIntent(domain, text)
        print(f"Intención {intent}")
        response, p = self.identifyResponse(intent, text)
        return domain, intent, p, response

    def identifyDomain(self, text):
        pass

    def identifyIntent(self, domain, text):
        pass

    def identifyResponse(self, intent, text):
        pass