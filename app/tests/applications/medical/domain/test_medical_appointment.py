from src.sso.domain.user import User
from src.applications.medical.domain.date import Date
from src.applications.medical.domain.medical_appointment import MedicalAppointment
from src.applications.medical.domain.medical_speciality import MedicalSpeciality


def test_construct():
    user: User = User("usuario de prueba")
    speciality: MedicalSpeciality = MedicalSpeciality("dermatólogo")
    date: Date = Date("22/03/1983-11:00")

    medicalAppointment: MedicalAppointment = MedicalAppointment(user, speciality, date)

    assert medicalAppointment.user.username == "usuario de prueba"
    assert medicalAppointment.speciality.name == "dermatólogo"
    assert date.date == "22/03/1983-11:00"
