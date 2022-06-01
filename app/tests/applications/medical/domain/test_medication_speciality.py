from src.applications.medical.domain.medical_speciality import MedicalSpeciality


def test_construct():
    medicationSpeciality = MedicalSpeciality("prueba")

    assert medicationSpeciality.name == "prueba"
