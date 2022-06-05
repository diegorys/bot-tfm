from src.applications.medical.domain.date import Date


def test_construct():
    date = Date("2022-11-22T12:00:00+02:00")

    assert date.date == "2022-11-22T12:00:00+02:00"
