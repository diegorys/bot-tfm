from conversational_bot.command_manager import CommandManager
from applications.medical.commands.add_medication_command import AddMedicationCommand
from applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase
from applications.medical.infrastructure.dynamodb_medication_repository import (
    DynamoDBMedicationRepository,
)
from events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository


class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        return commandManager

    def addMedicalCommands(commandManager: CommandManager):
        medRepository = DynamoDBMedicationRepository()
        eventsRepository = DynamoDBEventRepository()
        registerMedicationUseCase = RegisterMedicationUseCase(medRepository, eventsRepository)
        addMedicationCommand = AddMedicationCommand(registerMedicationUseCase)
        commandManager.addCommand("REGISTRAR_TOMA_MEDICAMENTO", addMedicationCommand)
