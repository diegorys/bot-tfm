from datetime import datetime, timedelta


class User:
    def __init__(self, username, metadata=None):
        self.username = username
        self.metadata = metadata
        if metadata is None:
            self.metadata = {}
        self.id = None
        self.relations = {}
        self.metadata["last_activity"] = 0
        self.metadata["active"] = False

    def setCaregiver(self, user):
        self.relations["caregiver"] = user
        self.metadata["caregiver"] = user.id

    def addDependent(self, user):
        if "dependents" not in self.relations.keys():
            self.relations["dependents"] = []
        if "dependents" not in self.metadata.keys():
            self.metadata["dependents"] = []
        self.relations["dependents"].append(user)
        self.metadata["dependents"].append(user.id)

    def markActive(self, active: bool) -> None:
        self.metadata["active"] = active

    def isMarkedAsActive(self) -> bool:
        return self.metadata["active"]

    def isActive(self) -> bool:
        last = self.metadata["last_activity"]
        threshold = (datetime.now() - timedelta(hours=3)).timestamp()
        return last > threshold

    def registerActivity(self) -> None:
        self.metadata["last_activity"] = datetime.now().timestamp()

    def isDependant(self):
        return "caregiver" in self.relations.keys()

    def isCaregiver(self):
        return "dependents" in self.relations.keys()

    def getCaregiver(self):
        if "caregiver" in self.relations.keys():
            return self.relations["caregiver"]
        return None

    def getDependents(self):
        if "dependents" in self.relations.keys():
            return self.relations["dependents"]
        return []

    def getKey(self, key):
        if key in self.metadata.keys():
            return self.metadata[key]
        return None

    def setKey(self, key: str, value: any):
        self.metadata[key] = value
