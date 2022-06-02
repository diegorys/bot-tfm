from tests.conversational_bot.mother.command_mother import CommandMother
from src.conversational_bot.frame import Frame
from src.conversational_bot.command import Command
from src.conversational_bot.command_manager import CommandManager
from tests.conversational_bot.mother.frame_mother import FrameMother


def test_addCommand():
    manager = CommandManager()

    manager.addCommand("one", None)

    assert "one" in manager.commands.keys()


def test_execute_existing():
    manager = CommandManager()
    command = CommandMother.getValid()
    frameRequest = FrameMother.getValid()
    manager.addCommand(frameRequest.intent, command)

    frameResponse = manager.execute(frameRequest)

    assert frameResponse == frameRequest


def test_execute_not_existing():
    manager = CommandManager()
    frameRequest = FrameMother.getValid()

    frameResponse = manager.execute(frameRequest)

    assert frameResponse == None
