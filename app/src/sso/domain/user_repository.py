from src.sso.domain.user import User


class UserRepository:
    def save(self, user: User):
        pass

    def list(self):
        pass

    def getByMetadata(self, key, value):
        pass
