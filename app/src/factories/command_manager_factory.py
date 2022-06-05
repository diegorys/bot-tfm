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


class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        CommandManagerFactory.addStatusCommands(commandManager)
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
        registerUserStatusUseCase = RegisterUserStatusUseCase(repository)
        askForUserStatusUseCase = AskForUserStatusUseCase(repository)
        registerCommand = RegisterUserStatusCommand(registerUserStatusUseCase)
        askCommand = AskForUserStatusCommand(askForUserStatusUseCase)
        commandManager.addCommand("REGISTRAR_ESTADO_EMOCIONAL", registerCommand)
        commandManager.addCommand("CONSULTAR_ESTADO_PERSONA_MAYOR", askCommand)
