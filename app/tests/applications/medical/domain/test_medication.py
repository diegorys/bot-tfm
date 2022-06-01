from src.applications.medical.domain.medication import Medication


def test_construct():
    medication = Medication("prueba")

    assert medication.name == "prueba"
