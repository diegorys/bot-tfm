class IntroduceOnself:
    def __init__(self, command):
        self.command = command

    def execute(self, user, text):
        return f"Hola {user.name}, soy tu cuidador, encantado de conocerte."
