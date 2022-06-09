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
            if key in user.metadata.keys() and str(value) == user.metadata[key]:
                foundUser = user
        if foundUser is None:
            raise Exception(f"User with metadata {key} - {value} not found")
        return self.addRelations(userDict, foundUser)

    def addRelations(self, userDict, user: User):
        if "caregiver" in list(user.metadata.keys()) and user.metadata["caregiver"] is not None:
            user.relations["caregiver"] = userDict[user.metadata["caregiver"]]
        if "dependents" in list(user.metadata.keys()) and user.metadata["dependents"] is not None:
            user.relations["dependents"] = []
            for dependent in list(user.metadata["dependents"]):
                if dependent is not None and userDict[str(dependent)] is not None:
                    user.addDependent(userDict[str(dependent)])
        return user

