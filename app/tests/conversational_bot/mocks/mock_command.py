from src.sso.domain.user import User
from src.conversational_bot.command import Command


class MockCommand(Command):
    def execute(self, user: User, args):
        return True
