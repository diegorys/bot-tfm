from datetime import datetime, timedelta


class User:
    def __init__(self, username, metadata={}):
        self.username = username
        self.metadata = metadata
        self.id = None
        self.relations = {}

    def markActive(self, active: bool) -> None:
        self.metadata["active"] = active

    def isMarkedAsActive(self) -> bool:
        return self.metadata["active"]

    def isActive(self) -> bool:
        last = self.metadata["last_activity"]
        threshold = (datetime.now() - timedelta(hours=3)).timestamp()
        return last < threshold

    def registerActivity(self) -> None:
        self.metadata["last_activity"] = datetime.now().timestamp()

    def isDependant(self):
        return "caregiver" in self.relations.keys()
