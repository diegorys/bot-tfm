from src.applications.medical.domain.medication_user import MedicationUser
from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository
from src.applications.medical.domain.medication_user_repository import MedicationUserRepository


class RegisterMedicationUseCase:
    def __init__(self, repository: MedicationUserRepository, eventRepository: EventRepository):
        self.repository = repository
        self.eventRepository = eventRepository

    def execute(self, medicationUser: MedicationUser):
        print(
            f"SAVE MEDICINE {medicationUser.medication.name} FOR USER {medicationUser.user.username} AT {medicationUser.date.date}"
        )
        event: Event = Event(
            medicationUser.user,
            "RECORDAR_MEDICACION",
            {"medicamento": medicationUser.medication.name},
            medicationUser.date.date,
        )
        saved = self.repository.save(medicationUser)
        self.eventRepository.save(event)
        return saved
