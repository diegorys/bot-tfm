from conversational_bot.domain.frame import Frame


class CommandManager:
    def __init__(self):
        pass

    def execute(self, frame: Frame) -> None:
        print(f"Manage command {frame.intent} with parameters:")
        print(frame.entities)
        return frame
