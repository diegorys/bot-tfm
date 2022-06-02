from src.sso.domain.user import User


class UserMother:
    def getValid():
        return User("usertest")
