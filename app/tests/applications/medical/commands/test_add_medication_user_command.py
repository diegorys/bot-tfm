import os
from src.applications.medical.domain.medication_user import MedicationUser
from tests.applications.medical.mothers.add_medication_user_command_mother import (
    AddMedicationUserCommandMother,
)
from tests.sso.mothers.user_mother import UserMother

os.environ["STAGE"] = "test"


def test_execute():
    command = AddMedicationUserCommandMother.getValid()
    user = UserMother.getValid()
    args = {"medicamento": "medicationtest", "cuando": "2022-11-22T12:00:00+02:00"}

    medicationUser: MedicationUser = command.execute(user, args)

    assert medicationUser.user.username == user.username
    assert medicationUser.medication.name == args["medicamento"]
    assert medicationUser.date.date == args["cuando"]
