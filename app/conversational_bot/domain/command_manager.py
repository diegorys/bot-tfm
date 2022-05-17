from conversational_bot.domain.frame import Frame


class CommandManager:
    def __init__(self):
        self.commands = {}

    def addCommand(self, commandName: str, function):
        self.commands[commandName] = function

    def execute(self, frame: Frame) -> None:
        print(f"Manage command {frame.intent} with parameters:")
        print(frame.entities)
        if frame.intent in self.commands.keys():
            self.commands[frame.intent](frame.entities)
        else:
            print(f"[Warning][CommandManager][execute] Command {frame.intent} not found")

        return frame
