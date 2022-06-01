from src.sso.domain.user import User
from src.applications.medical.domain.date import Date
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.medication import Medication


def test_construct():
    user: User = User("usuario de prueba")
    medication: Medication = Medication("medicación de prueba")
    date: Date = Date("22/03/1983-11:00")

    medicationUser: MedicationUser = MedicationUser(user, medication, date)

    assert medicationUser.user.username == "usuario de prueba"
    assert medicationUser.medication.name == "medicación de prueba"
    assert date.date == "22/03/1983-11:00"
