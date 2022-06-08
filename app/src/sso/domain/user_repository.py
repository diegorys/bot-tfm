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
        return self.addRelations(userDict, foundUser)

    def addRelations(self, userDict, user):
        if "caregiver" in list(user.metadata.keys()):
            user.relations["caregiver"] = userDict[user.metadata["caregiver"]]
        if "dependents" in list(user.metadata.keys()):
            user.relations["dependents"] = []
            for dependent in list(user.metadata["dependents"]):
                user.relations["dependents"].append(userDict[str(dependent)])
        return user

