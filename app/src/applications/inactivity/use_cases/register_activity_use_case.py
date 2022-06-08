from datetime import datetime
from src.sso.domain.user import User
from src.sso.domain.user_repository import UserRepository


class RegisterActivityUseCase:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def execute(self, user: User):
        user.metadata["last_activity"] = datetime.now().timestamp()
        self.userRepository.save(user)
