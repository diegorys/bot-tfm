class NLU:
    def __init__(self, knowledgeRepository):
        self.intents = {}
        self.knowledgeRepository = knowledgeRepository

    def handle(self, action):
        self.intents[action.command] = action

    def executeCommand(self, user, command):
        action = self.intents[command]
        return action.execute(user, command)

    def getResponse(self, text):
        pass

    def identifyDomain(self, text):
        pass

    def identifyIntent(self, domain, text):
        pass

    def identifyResponse(self, intent, text):
        pass

    def generateText(self, request):
        pass