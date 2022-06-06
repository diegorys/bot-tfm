from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase
from src.sso.domain.user import User
from src.conversational_bot.command import Command


class AskForUserStatusCommand(Command):
    def __init__(self, useCase: AskForUserStatusUseCase):
        self.useCase = useCase

    def execute(self, user: User, args):
        print(f"AskForUserStatusCommand execute")
        return self.useCase.execute(user)
