from src.conversational_bot.response import Response
from src.sso.domain.user import User


class Command:
    def execute(self, user: User, args) -> Response or None:
        pass
