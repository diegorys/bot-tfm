from conversational_bot.command import Command
from applications.medical.use_cases.register_medication_use_case import RegisterMedicationUseCase


class AddMedicationCommand(Command):
    def __init__(self, useCase: RegisterMedicationUseCase):
        self.useCase = useCase

    def execute(self, args):
        print(f"AddMedicationCommand execute")
        medication = args["medicamento"]
        dateTime = args["date-time"]
        self.useCase.execute(medication, dateTime)
        print(args)
