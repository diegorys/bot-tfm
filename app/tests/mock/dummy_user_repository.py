from sso.domain.user import User
from sso.domain.user_repository import UserRepository


class DummyUsersRepository(UserRepository):
    def save(self, user: User):
        return user

    def list(self):
        return [
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
