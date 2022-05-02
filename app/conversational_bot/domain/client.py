from sso.domain.user import User


class Client:
    def handle(self, text: str) -> None:
        pass

    def emit(self, user: User, text: str) -> None:
        pass
