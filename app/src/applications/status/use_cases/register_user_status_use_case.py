from src.applications.status.domain.user_in_status_repository import UserInStatusRepository
from src.applications.status.domain.user_in_status import UserInStatus


class RegisterUserStatusUseCase:
    def __init__(self, repository: UserInStatusRepository):
        self.repository = repository

    def execute(self, userInStatus: UserInStatus):
        saved = self.repository.save(userInStatus)
        return saved
