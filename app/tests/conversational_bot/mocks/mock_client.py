from src.sso.domain.user import User
from src.conversational_bot.client import Client


class MockClient(Client):
    def __init__(self):
        self.mockText = ""
        self.mockUser = None
        self.count = 0
        self.mockTexts = []

    def emit(self, user: User, text: str):
        self.mockText = text
        self.mockUser = user
        self.count += 1
        self.mockTexts.append(text)
