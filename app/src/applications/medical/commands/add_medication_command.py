from src.sso.domain.user import User
from src.conversational_bot.command import Command
from src.applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase


class AddMedicationCommand(Command):
    def __init__(self, useCase: RegisterMedicationUseCase):
        self.useCase = useCase

    def execute(self, user: User, args):
        print(f"AddMedicationCommand execute")
        medication = args["medicamento"]
        medicationUser = {
            "medication": medication,
            "user": user
        }
        dateTime = args["date-time"]
        self.useCase.execute(medication, dateTime)
        print(args)
