import os
from src.applications.medical.domain.medical_appointment import MedicalAppointment
from tests.applications.medical.mothers.add_medical_appointment_command_mother import AddMedicalAppointmentCommandMother
from tests.sso.mothers.user_mother import UserMother

os.environ["STAGE"] = "test"

def test_execute():
    command = AddMedicalAppointmentCommandMother.getValid()
    user = UserMother.getValid()
    args = {"cita": "especialidadtest", "cuando": "18:00"}

    appointment: MedicalAppointment = command.execute(user, args)

    assert appointment.user.username == user.username
    assert appointment.speciality.name == args["cita"]
    assert appointment.date.date == args["cuando"]
