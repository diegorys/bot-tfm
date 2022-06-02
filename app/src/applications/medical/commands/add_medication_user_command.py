from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.domain.date import Date
from src.applications.medical.domain.medication import Medication
from src.sso.domain.user import User
from src.conversational_bot.command import Command
from src.applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase


class AddMedicationUserCommand(Command):
    def __init__(self, useCase: RegisterMedicationUseCase):
        self.useCase = useCase

    def execute(self, user: User, args):
        print(f"AddMedicationCommand execute")
        medication = Medication(args["medicamento"])
        dateTime = Date(args["date-time"])
        medicationUser = MedicationUser(user, medication, dateTime)

        return self.useCase.execute(medicationUser)
