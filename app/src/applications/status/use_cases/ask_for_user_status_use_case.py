from src.sso.domain.user import User
from src.applications.status.domain.user_in_status_repository import UserInStatusRepository
from src.applications.status.domain.user_in_status import UserInStatus


class AskForUserStatusUseCase:
    def __init__(self, repository: UserInStatusRepository):
        self.repository = repository

    def execute(self, user: User):
        pass
