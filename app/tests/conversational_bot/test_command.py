from src.conversational_bot.command import Command

def test_command_execute():
    command = Command()

    command.execute(None, {})

    assert type(command) == Command