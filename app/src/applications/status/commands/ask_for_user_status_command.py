from datetime import datetime
from src.applications.status.domain.user_in_status import UserInStatus
from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase
from src.sso.domain.user import User
from src.conversational_bot.command import Command
from src.applications.status.domain.status import Status
from src.applications.status.use_cases.register_user_status_use_case import (
    RegisterUserStatusUseCase,
)


class AskForUserStatusCommand(Command):
    def __init__(self, useCase: AskForUserStatusUseCase):
        self.useCase = useCase

    def execute(self, user: User, args):
        print(f"AskForUserStatusCommand execute")
        # TODO: usuarios al cuidado
        return self.useCase.execute(user)
