from src.conversational_bot.command_manager import CommandManager
from src.applications.medical.commands.add_medication_user_command import AddMedicationUserCommand
from src.applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase
from src.applications.medical.infrastructure.dynamodb_medication_repository import (
    DynamoDBMedicationRepository,
)
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository


class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        return commandManager

    def addMedicalCommands(commandManager: CommandManager):
        medRepository = DynamoDBMedicationRepository()
        eventsRepository = DynamoDBEventRepository()
        registerMedicationUseCase = RegisterMedicationUseCase(medRepository, eventsRepository)
        addMedicationCommand = AddMedicationUserCommand(registerMedicationUseCase)
        commandManager.addCommand("REGISTRAR_TOMA_MEDICAMENTO", addMedicationCommand)
