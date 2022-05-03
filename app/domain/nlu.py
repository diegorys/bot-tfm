from conversational_bot.domain.response import Response


class NLU:
    def __init__(self):
        self.domains = {}

    def handle(self, action):
        self.domains[action.intent] = action

    def getResponse(self, user, request):
        print("DOMINIO DE " + request)
        intent = self.identifyIntent(request)
        print("IDENTIFICADA INTENCIÓN: " + intent)
        response = Response(user, "No entiendo")
        if intent in list(self.domains.keys()):
            response = self.domains[intent].execute(user, request)
        return response

    def executeCommand(self, user, command):
        action = self.domains[command]
        return action.execute(user, command)
