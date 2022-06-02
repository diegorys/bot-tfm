from src.applications.medical.domain.medication_user_repository import MedicationUserRepository
from src.applications.medical.domain.medication_user import MedicationUser


class MockMedicationUserRepository(MedicationUserRepository):
    def save(self, medicationUser: MedicationUser):
        return medicationUser
