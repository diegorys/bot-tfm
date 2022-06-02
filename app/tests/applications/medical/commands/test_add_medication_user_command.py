from src.applications.medical.domain.medication_user import MedicationUser
from tests.applications.medical.mothers.add_medication_user_command_mother import AddMedicationUserCommandMother
from tests.sso.mothers.user_mother import UserMother


def test_execute():
    command = AddMedicationUserCommandMother.getValid()
    user = UserMother.getValid()
    args = {"medicamento": "medicationtest", "date-time": "18:00"}

    medicationUser: MedicationUser = command.execute(user, args)

    assert medicationUser.user.username == user.username
    assert medicationUser.medication.name == args["medicamento"]
    assert medicationUser.date.date == args["date-time"]
