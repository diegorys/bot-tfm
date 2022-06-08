from src.sso.domain.user import User


class UserMother:
    def getValid(userName: str = "usertest") -> User:
        return User(userName)

    def getPairCaregiverDependentWithNames(caregiverName: str, dependantName: str):
        caregiver = UserMother.getValid(caregiverName)
        dependent = UserMother.getValid(dependantName)
        dependent.relations["caregiver"] = caregiver
        caregiver.relations["dependents"] = [dependent]
        return caregiver, dependent
