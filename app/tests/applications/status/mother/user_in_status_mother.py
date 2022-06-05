from datetime import datetime
from src.applications.status.domain.status import Status
from src.applications.status.domain.user_in_status import UserInStatus
from tests.sso.mothers.user_mother import UserMother

class UserInStatusMother:

    def forStatusNow(status: str):
        user = UserMother.getValid()
        user.metadata["telegram_id"] = "1234"
        status = Status(status)
        userInStatus = UserInStatus(user, status, datetime.now().timestamp())
        return userInStatus