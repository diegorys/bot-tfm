from datetime import datetime, timedelta


class User:
    def __init__(self, username, metadata = None):
        self.username = username
        self.metadata = metadata
        if metadata is None:
            self.metadata = {}            
        self.id = None
        self.relations = {}
        self.metadata["last_activity"] = 0
        self.metadata["active"] = False

    def markActive(self, active: bool) -> None:
        last = self.metadata["last_activity"]
        self.metadata["active"] = active
        last = self.metadata["last_activity"]

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
