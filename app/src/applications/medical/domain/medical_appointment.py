from src.applications.medical.domain.date import Date
from src.sso.domain.user import User
from src.applications.medical.domain.medical_speciality import MedicalSpeciality


class MedicalAppointment:
    def __init__(self, user: User, speciality: MedicalSpeciality, date: Date):
        self.user = user
        self.speciality = speciality
        self.date = date
