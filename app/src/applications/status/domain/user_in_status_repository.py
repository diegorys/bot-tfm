from abc import abstractmethod
from src.sso.domain.user import User
from src.applications.status.domain.user_in_status import UserInStatus


class UserInStatusRepository:
    @abstractmethod
    def save(userInStatus: UserInStatus):
        pass

    @abstractmethod
    def getStatusOf(self, user: User) -> UserInStatus:
        pass
