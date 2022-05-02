from sso.domain.user import User
from conversational_bot.domain.client import Client


class DummyClient(Client):
    def __init__(self):
        self.dummyText = ""
        self.dummyUser = None

    def emit(self, user: User, text: str):
        self.dummyText = text
        self.dummyUser = user
