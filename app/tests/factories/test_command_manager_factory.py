from src.conversational_bot.command_manager import CommandManager
from src.factories.command_manager_factory import CommandManagerFactory


def test_command_manager_factory_create():
    factory = CommandManagerFactory

    commandManager = factory.create()

    assert isinstance(commandManager, CommandManager)


def test_addMedicalCommands():
    commandManager = CommandManager()

    CommandManagerFactory.addMedicalCommands(commandManager)

    assert "REGISTRAR_TOMA_MEDICAMENTO" in commandManager.commands.keys()
