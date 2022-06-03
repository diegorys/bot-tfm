from src.applications.medical.use_cases.register_medical_appointment_use_case import RegisterMedicalAppointmentUseCase
from src.conversational_bot.command_manager import CommandManager
from src.applications.medical.commands.add_medication_user_command import AddMedicationUserCommand
from src.applications.medical.commands.add_medical_appointment_command import AddMedicalAppointmentCommand
from src.applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase
from src.applications.medical.infrastructure.dynamodb_medication_user_repository import (
    DynamoDBMedicationUserRepository,
)
from src.applications.medical.infrastructure.dynamodb_medical_appointment_repository import (
    DynamoDBMedicalAppointmentRepository,
)
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository


class CommandManagerFactory:
    def create():
        commandManager = CommandManager()
        CommandManagerFactory.addMedicalCommands(commandManager)
        return commandManager

    def addMedicalCommands(commandManager: CommandManager):
        medicationUserRepository = DynamoDBMedicationUserRepository()
        eventsRepository = DynamoDBEventRepository()
        registerMedicationUseCase = RegisterMedicationUseCase(medicationUserRepository, eventsRepository)
        addMedicationCommand = AddMedicationUserCommand(registerMedicationUseCase)
        commandManager.addCommand("REGISTRAR_TOMA_MEDICAMENTO", addMedicationCommand)
        medicalAppointmentRepository = DynamoDBMedicalAppointmentRepository()
        registerMedicalAppointmentUseCase = RegisterMedicalAppointmentUseCase(medicalAppointmentRepository, eventsRepository)
        addMedicalAppointmentCommand = AddMedicalAppointmentCommand(registerMedicalAppointmentUseCase)
        commandManager.addCommand("REGISTRAR_CITA_MEDICA", addMedicalAppointmentCommand)