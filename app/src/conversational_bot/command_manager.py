from src.conversational_bot.frame import Frame
from src.conversational_bot.command import Command


class CommandManager:
    def __init__(self):
        self.commands = {}

    def addCommand(self, commandName: str, command: Command):
        self.commands[commandName] = command

    def execute(self, frame: Frame) -> Frame or None:
        print(f"Manage command '{frame.intent}' with parameters:")
        if frame.intent in self.commands.keys():
            try:
                self.commands[frame.intent].execute(frame.user, frame.entities)
            except Exception as e:
                print(f"[Error][CommandManager][execute] Command {frame.intent} fails")
                print(e)  
        else:
            print(f"[Warning][CommandManager][execute] Command {frame.intent} not found")
            return None

        return frame
