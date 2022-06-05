from src.sso.domain.user import User
from src.applications.status.domain.status import Status


class UserInStatus:
    def __init__(self, user: User, status: Status, timestamp: float):
        self.user = user
        self.status = status
        self.timestamp = timestamp
