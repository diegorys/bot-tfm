class User:
    def __init__(self, username, metadata={}):
        self.username = username
        self.metadata = metadata
        self.id = None
        self.relations = {}
