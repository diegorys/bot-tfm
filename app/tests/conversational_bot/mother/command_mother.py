from src.conversational_bot.command import Command
from tests.conversational_bot.mocks.mock_command import MockCommand


class CommandMother:
    def getValid() -> Command:
        command = MockCommand()
        return command
