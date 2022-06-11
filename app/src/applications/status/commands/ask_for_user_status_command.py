from src.sso.domain.user import User
from src.conversational_bot.response import Response
from src.conversational_bot.command import Command
from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase

class AskForUserStatusCommand(Command):
    def __init__(self, useCase: AskForUserStatusUseCase):
        self.useCase = useCase

    def execute(self, user: User, args) -> Response or None:
        print(f"AskForUserStatusCommand execute")
        return self.useCase.execute(user)
