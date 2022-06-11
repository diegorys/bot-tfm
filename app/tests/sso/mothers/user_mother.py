from src.sso.domain.user import User


class UserMother:
    def getValid(userName: str = "usertest") -> User:
        return User(userName)

    def forId(id: str) -> User:
        user = UserMother.getValid()
        user.id = id
        return user

    def getPairCaregiverDependentWithNames(caregiverName: str, dependantName: str):
        caregiver = UserMother.getValid(caregiverName)
        dependent = UserMother.getValid(dependantName)
        dependent.setCaregiver(caregiver)
        caregiver.addDependent(dependent)
        return caregiver, dependent
