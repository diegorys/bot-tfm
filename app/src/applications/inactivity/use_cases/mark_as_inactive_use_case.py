from datetime import datetime
from src.sso.domain.user_repository import UserRepository
from src.sso.domain.user import User


class MarkASInactiveUseCase:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    # Execute at 13:00 and at 20:00. Checks 3 hours of inactivity.
    def execute(self):
        users = self.userRepository.list()
        for user in users:
            dependant: User = user
            if dependant.isDependant() and not dependant.isActive():
                dependant.markActive(False)
            else:
                dependant.markActive(True)
