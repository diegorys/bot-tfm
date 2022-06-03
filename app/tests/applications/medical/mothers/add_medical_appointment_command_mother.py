from src.applications.medical.commands.add_medical_appointment_command import AddMedicalAppointmentCommand
from src.applications.medical.use_cases.register_medical_appointment_use_case import (
    RegisterMedicalAppointmentUseCase,
)
from tests.applications.medical.mocks.mock_medical_appointment_repository import (
    MockMedicalAppointmentRepository,
)
from tests.events.mocks.mock_event_repository import MockEventRepository


class AddMedicalAppointmentCommandMother:
    def getValid():
        repository = MockMedicalAppointmentRepository()
        events = MockEventRepository()
        useCase = RegisterMedicalAppointmentUseCase(repository, events)
        command = AddMedicalAppointmentCommand(useCase)
        return command
