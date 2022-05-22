from conversational_bot.frame import Frame
from conversational_bot.command import Command


class CommandManager:
    def __init__(self):
        self.commands = {}

    def addCommand(self, commandName: str, command: Command):
        self.commands[commandName] = command
        print(self.commands.keys())

    def execute(self, frame: Frame) -> None:
        print(f"Manage command '{frame.intent}' with parameters:")
        print(frame.entities)
        print(self.commands.keys())
        if frame.intent in self.commands.keys():
            self.commands[frame.intent].execute(frame.entities)
        else:
            print(f"[Warning][CommandManager][execute] Command {frame.intent} not found")

        return frame
