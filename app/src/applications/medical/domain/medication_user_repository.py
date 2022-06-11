from abc import abstractmethod
from src.applications.medical.domain.medication_user import MedicationUser


class MedicationUserRepository:
    @abstractmethod
    def save(self, medicationUser: MedicationUser):
        pass
