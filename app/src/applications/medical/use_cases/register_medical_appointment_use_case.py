from src.events.domain.event import Event
from src.events.domain.event_repository import EventRepository
from src.applications.medical.domain.medical_appointment_repository import (
    MedicalAppointmentRepository,
)
from src.applications.medical.domain.medical_appointment import MedicalAppointment


class RegisterMedicalAppointmentUseCase:
    def __init__(self, repository: MedicalAppointmentRepository, eventRepository: EventRepository):
        self.repository = repository
        self.eventRepository = eventRepository

    def execute(self, medicalAppointment: MedicalAppointment):
        print(
            f"SAVE MEDICAL APPOINTMENT {medicalAppointment.speciality.name} AT {medicalAppointment.date.date}"
        )
        event: Event = Event(
            "RECORDAR_CITA_MEDICA",
            medicalAppointment.user,
            {"cita": medicalAppointment.speciality.name},
            medicalAppointment.date.date,
        )
        saved = self.repository.save(medicalAppointment)
        self.eventRepository.save(event)
        return saved
