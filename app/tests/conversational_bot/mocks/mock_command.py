from src.sso.domain.user import User
from src.conversational_bot.command import Command


class MockCommand(Command):
    def __init__(self, raiseException=False):
        self.raiseException = raiseException

    def execute(self, user: User, args):
        if self.raiseException:
            raise Exception("raised from command")
        return True
