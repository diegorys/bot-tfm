from src.applications.medical.domain.medication_user_repository import MedicationUserRepository
from src.applications.medical.domain.medical_appointment import MedicalAppointment


class MockMedicalAppointmentRepository(MedicationUserRepository):
    def save(self, medicalAppointment: MedicalAppointment):
        return medicalAppointment
