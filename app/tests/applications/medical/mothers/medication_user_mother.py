from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.date import Date
from tests.applications.medical.mothers.medication_mother import MedicationMother
from tests.sso.mothers.user_mother import UserMother


class MedicationUserMother:
    def getValid():
        user = UserMother.getValid()
        medication = MedicationMother.getValid()
        date = Date("18:00")
        medicationUser = MedicationUser(user, medication, date)
