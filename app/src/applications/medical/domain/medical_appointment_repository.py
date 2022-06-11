from abc import abstractmethod
from src.applications.medical.domain.medical_appointment import MedicalAppointment


class MedicalAppointmentRepository:
    @abstractmethod
    def save(self, medicalAppointment: MedicalAppointment):
        pass
