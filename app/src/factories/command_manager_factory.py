import os
from src.applications.inactivity.commands.register_activity_command import RegisterActivityCommand
from src.applications.inactivity.use_cases.register_activity_use_case import (
    RegisterActivityUseCase,
)
from src.applications.medical.use_cases.register_medical_appointment_use_case import (
    RegisterMedicalAppointmentUseCase,
)
from src.conversational_bot.command_manager import CommandManager
from src.applications.medical.commands.add_medication_user_command import AddMedicationUserCommand
from src.applications.medical.commands.add_medical_appointment_command import (
    AddMedicalAppointmentCommand,
)
from src.applications.medical.use_cases.register_medication_use_case import (
    RegisterMedicationUseCase,
)
from src.applications.medical.infrastructure.dynamodb_medication_user_repository import (
    DynamoDBMedicationUserRepository,
)
from src.applications.medical.infrastructure.dynamodb_medical_appointment_repository import (
    DynamoDBMedicalAppointmentRepository,
)
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository
from src.applications.status.infrastructure.dynamodb_user_in_status_repository import (
    DynamoDBUserInStatusRepository,
)
from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase
from src.applications.status.use_cases.register_user_status_use_case import (
    RegisterUserStatusUseCase,
)
from src.applications.status.commands.ask_for_user_status_command import (
    AskForUserStatusCommand,
    AskForUserStatusUseCase,
)
from src.applications.status.commands.register_user_status_command import RegisterUserStatusCommand
from src.sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository
from src.interfaces.telegram_client import TelegramClient

class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        CommandManagerFactory.addStatusCommands(commandManager)
        CommandManagerFactory.addInactivityCommands(commandManager)
        return commandManager

    def addMedicalCommands(commandManager: CommandManager):
        medicationUserRepository = DynamoDBMedicationUserRepository()
        eventsRepository = DynamoDBEventRepository()
        registerMedicationUseCase = RegisterMedicationUseCase(
            medicationUserRepository, eventsRepository
        )
        addMedicationCommand = AddMedicationUserCommand(registerMedicationUseCase)
        commandManager.addCommand("REGISTRAR_TOMA_MEDICAMENTO", addMedicationCommand)
        medicalAppointmentRepository = DynamoDBMedicalAppointmentRepository()
        registerMedicalAppointmentUseCase = RegisterMedicalAppointmentUseCase(
            medicalAppointmentRepository, eventsRepository
        )
        addMedicalAppointmentCommand = AddMedicalAppointmentCommand(
            registerMedicalAppointmentUseCase
        )
        commandManager.addCommand("REGISTRAR_CITA_MEDICA", addMedicalAppointmentCommand)

    def addStatusCommands(commandManager: CommandManager):
        repository = DynamoDBUserInStatusRepository()
        TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
        client = TelegramClient(TELEGRAM_TOKEN)
        registerUserStatusUseCase = RegisterUserStatusUseCase(repository, client)
        askForUserStatusUseCase = AskForUserStatusUseCase(repository)
        registerCommand = RegisterUserStatusCommand(registerUserStatusUseCase)
        askCommand = AskForUserStatusCommand(askForUserStatusUseCase)
        commandManager.addCommand("REGISTRAR_ESTADO_EMOCIONAL", registerCommand)
        commandManager.addCommand("CONSULTAR_ESTADO_PERSONA_MAYOR", askCommand)

    def addInactivityCommands(commandManager: CommandManager):
        repository = DynamoDBUsersRepository()
        useCase = RegisterActivityUseCase(repository)
        command = RegisterActivityCommand(useCase)
        commandManager.addCommand("*", command)
