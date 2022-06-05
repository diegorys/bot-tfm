from src.sso.domain.user import User
from src.applications.status.domain.user_in_status import UserInStatus


class UserInStatusRepository:
    def save(userInStatus: UserInStatus):
        pass

    def getStatusOf(self, user: User):
        pass
