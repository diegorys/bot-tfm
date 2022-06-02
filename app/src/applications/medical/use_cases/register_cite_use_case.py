from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository


class RegisterMedicationUseCase:
    def __init__(self, repository: MedicationUserRepository, eventRepository: EventRepository):
        self.repository = repository
        self.eventRepository = EventRepository

    def execute(self, medicationUser, datetime):
        print(f"SAVE MEDICINE {medicationUser.name} AT {datetime}")
        event: Event = Event(
            "RECORDAR_MEDICACION", medicationUser.user, medicationUser.medication, datetime
        )
        self.repository.save(medicationUser)
        self.eventRepository.save(event)
