from conversational_bot.domain.command_manager import CommandManager
from medical.commands.add_medication_command import AddMedicationCommand
from medical.use_cases.register_medication_use_case import RegisterMedicationUseCase


class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        return commandManager
    

    def addMedicalCommands(commandManager: CommandManager):
        registerMedicationUseCase = RegisterMedicationUseCase()
        addMedicationCommand = AddMedicationCommand(registerMedicationUseCase)
        commandManager.addCommand("REGISTRAR_TOMA_MEDICAMENTO", addMedicationCommand)