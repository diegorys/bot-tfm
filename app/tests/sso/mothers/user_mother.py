from src.sso.domain.user import User


class UserMother:
    def getValid() -> User:
        return User("usertest")

    def getPairCaregiverDependentWithDependentName(dependantName: str):
        caregiver = UserMother.getValid()
        dependent = UserMother.getValid()
        dependent.relations["caregiver"] = caregiver
        caregiver.relations["dependents"] = [dependent]
        return caregiver, dependent
