from src.conversational_bot.frame import Frame
from src.sso.domain.user import User
from tests.conversational_bot.mother.frame_mother import FrameMother

def test_add_entity():
    frame = FrameMother.getValid()

    frame.addEntity("test", "value")

    assert "test" in frame.entities.keys()
    assert frame.entities["test"] == "value"

def test_generate_ok():
    frame = Frame(
        "REGISTRAR_TOMA_MEDICAMENTO",
        User("diego"),
        "",
        {"medicamento": "ibuprofeno", "cuando": "a las 3"},
    )
    expected = "Tienes que tomar ibuprofeno a las 3"

    received = frame.generate("Tienes que tomar [medicamento] [cuando]")

    assert received == expected


def test_is_complete_true():
    frame = FrameMother.getValid()

    frame.addEntity("test", "value")

    assert frame.isComplete() == True


def test_is_complete_false():
    frame = FrameMother.getValid()

    frame.addEntity("test", None)

    assert frame.isComplete() == False