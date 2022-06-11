from src.sso.domain.user import User
from src.applications.status.domain.user_in_status import UserInStatus
from src.applications.status.domain.user_in_status_repository import UserInStatusRepository


class MockUserInStatusRepository(UserInStatusRepository):
    def __init__(self):
        self._list = []

    def save(self, userInStatus: UserInStatus):
        self._list.append(userInStatus)

    def getStatusOf(self, user: User) -> UserInStatus:
        for item in self._list:
            userInStatus: UserInStatus = item
            if user.id == userInStatus.user.id:
                return userInStatus
