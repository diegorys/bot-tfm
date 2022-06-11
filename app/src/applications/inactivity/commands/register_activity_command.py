from src.sso.domain.user import User
from src.conversational_bot.response import Response
from src.conversational_bot.command import Command
from src.applications.inactivity.use_cases.register_activity_use_case import RegisterActivityUseCase


class RegisterActivityCommand(Command):
    def __init__(self, useCase: RegisterActivityUseCase):
        self.useCase = useCase

    def execute(self, user: User, args) -> Response or None:
        print(f"RegisterActivityCommand execute")
        self.useCase.execute(user)
