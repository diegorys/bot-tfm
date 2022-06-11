from abc import abstractmethod
from src.sso.domain.user import User


class Client:
    @abstractmethod
    def emit(self, user: User, text: str) -> None:
        pass
