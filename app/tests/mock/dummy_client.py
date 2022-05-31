from src.sso.domain.user import User
from src.conversational_bot.client import Client


class DummyClient(Client):
    def __init__(self):
        self.dummyText = ""
        self.dummyUser = None
        self.count = 0

    def emit(self, user: User, text: str):
        self.dummyText = text
        self.dummyUser = user
        self.count += 1