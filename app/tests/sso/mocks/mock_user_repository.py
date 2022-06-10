from src.sso.domain.user import User
from src.sso.domain.user_repository import UserRepository


class MockUsersRepository(UserRepository):
    def __init__(self):
        self.users = [
            User(
                "Diego",
                {
                    "telegram_id": 1009284987,
                    "username": "Diego",
                    "caregiver": "",
                    "dependents": [1],
                },
            )
        ]

    def mockWith(self, users):
        self.users = users

    def save(self, user: User):
        return user

    def list(self):
        return self.users
