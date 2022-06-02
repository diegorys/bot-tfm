from src.applications.medical.commands.add_medication_user_command import AddMedicationUserCommand
from src.applications.medical.use_cases.register_medication_use_case import (
    RegisterMedicationUseCase,
)
from tests.applications.medical.mocks.mock_medication_user_repository import MockMedicationUserRepository
from tests.events.mocks.mock_event_repository import MockEventRepository


class AddMedicationUserCommandMother:
    def getValid():
        repository = MockMedicationUserRepository()
        events = MockEventRepository()
        useCase = RegisterMedicationUseCase(repository, events)
        command = AddMedicationUserCommand(useCase)
        return command
