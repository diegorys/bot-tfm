from conversational_bot.domain.client import Client


class DummyClient(Client):
    def __init__(self):
        self.dummyText = ""

    def emit(self, user, text):
        self.dummyText = text
