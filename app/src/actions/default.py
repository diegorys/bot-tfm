class Default:
    def __init__(self, command):
        self.command = command

    def execute(self, user, text):
        return f"{user.name}, no sé qué significa \"{text}\""
