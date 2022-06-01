from src.applications.medical.domain.date import Date


def test_construct():
    date = Date("prueba")

    assert date.date == "prueba"
