from src.applications.medical.domain.medical_appointment import MedicalAppointment
from src.applications.medical.domain.date import Date
from src.applications.medical.domain.medical_speciality import MedicalSpeciality
from src.sso.domain.user import User
from src.conversational_bot.command import Command
from src.applications.medical.use_cases.register_medical_appointment_use_case import RegisterMedicalAppointmentUseCase


class AddMedicalAppointmentCommand(Command):
    def __init__(self, useCase: RegisterMedicalAppointmentUseCase):
        self.useCase = useCase

    def execute(self, user: User, args):
        print(f"AddMedicalAppointmentCommand execute")
        speciality = MedicalSpeciality(args["cita"])
        dateTime = Date(args["cuando"])
        medicalAppointment = MedicalAppointment(user, speciality, dateTime)

        return self.useCase.execute(medicalAppointment)
