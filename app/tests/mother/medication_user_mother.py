from tests.mother.medication_mother import MedicationMother
from tests.mother.user_mother import UserMother
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.date import Date


class MedicationUserMother:
    def getValid():
        user = UserMother.getValid()
        medication = MedicationMother.getValid()
        date = Date("18:00")
        medicationUser = MedicationUser(user, medication, date)
