from src.events.use_cases.remember_use_case import RememberUseCase


def test_remember_use_case_formatResponse():
    useCase = RememberUseCase(None, None)
    event = {
        "id": "1654353071.5184305",
        "createdAt": "1654353071.5709345",
        "date": "2022-06-04T17:01:11+02:00",
        "entities": {"medicamento": "rinialer"},
        "intent": "RECORDAR_MEDICACION",
        "updatedAt": "1654353071.5709345",
        "user": "1009284987",
    }

    expected = "RECORDAR_MEDICACION, 17:01: medicamento rinialer"

    received = useCase.formatResponse(event)

    assert received == expected
