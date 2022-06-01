from src.applications.medical.domain.date import Date
from src.sso.domain.user import User
from src.applications.medical.domain.medication import Medication


class MedicationUser:
    def __init__(self, user: User, medication: Medication, date: Date):
        self.user = user
        self.medication = medication
        self.date = date
