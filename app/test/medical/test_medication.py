from medical.domain.medication import Medication


def test_fromCommand1():
    medication = Medication.fromCommand(
        "recordar-medicamento medicamento='ibuprofeno' hora='8:00' frecuencia='semanal'"
    )
    assert medication.name == "ibuprofeno"
    assert medication.hour == "8:00"
    assert medication.day == ""
    assert medication.frecuency == "semanal"


def test_fromCommand2():
    medication = Medication.fromCommand(
        "recordar-medicamento medicamento='calcio' dia='lunes' hora='18:30'"
    )
    assert medication.name == "calcio"
    assert medication.hour == "18:30"
    assert medication.day == "lunes"
    assert medication.frecuency == ""
