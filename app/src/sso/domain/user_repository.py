from src.sso.domain.user import User


class UserRepository:
    def save(self, user: User):
        pass

    def list(self):
        pass

    def getByMetadata(self, key, value):
        users = self.list()
        userDict = {}
        for user in users:
            userDict[user.id] = user
        foundUser = None
        for user in users:
            if str(value) == user.metadata[key]:
                foundUser = user
        if foundUser is None:
            raise Exception(f"User with metadata {key} - {value} not found")
        if "caregiver" in list(foundUser.metadata.keys()):
            foundUser.relations["caregiver"] = userDict[foundUser.metadata["caregiver"]]
        if "dependents" in list(foundUser.metadata.keys()):
            foundUser.relations["dependents"] = []
            for dependent in list(foundUser.metadata["dependents"]):
                foundUser.relations["dependents"].append(userDict[str(dependent)])
        return foundUser

