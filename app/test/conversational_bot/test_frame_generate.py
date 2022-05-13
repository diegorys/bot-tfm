import pytest
from conversational_bot.domain.frame import Frame
from sso.domain.user import User


def test_execute_ok():
    frame = Frame(
        "REGISTRAR_TOMA_MEDICAMENTO",
        User("diego"),
        "",
        {"medicamento": "ibuprofeno", "cuando": "a las 3"},
    )
    expected = "Tienes que tomar ibuprofeno a las 3"

    received = frame.generate("Tienes que tomar [medicamento] [cuando]")

    assert received == expected


@pytest.mark.skip(reason="Por ahora consideramos frames válidos")
def test_execute_ko():
    frame = Frame(
        "REGISTRAR_TOMA_MEDICAMENTO",
        User("diego"),
        "",
        {"cosa": "ibuprofeno", "cuando": "a las 3"},
    )
    expected = "Necesito que me indices medicamento"

    received = frame.generate("Tienes que tomar [medicamento] [cuando]")

    assert received == expected
