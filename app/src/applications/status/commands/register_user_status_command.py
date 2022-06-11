from datetime import datetime
from src.applications.status.domain.user_in_status import UserInStatus
from src.sso.domain.user import User
from src.conversational_bot.response import Response
from src.conversational_bot.command import Command
from src.applications.status.domain.status import Status
from src.applications.status.use_cases.register_user_status_use_case import (
    RegisterUserStatusUseCase,
)


class RegisterUserStatusCommand(Command):
    def __init__(self, useCase: RegisterUserStatusUseCase):
        self.useCase = useCase

    def execute(self, user: User, args) -> Response or None:
        print(f"RegisterUserStatusCommand execute")
        status = Status(args["estado"])
        userInStatus = UserInStatus(user, status, datetime.now().timestamp())
        self.useCase.execute(userInStatus)
