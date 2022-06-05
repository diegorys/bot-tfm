from tests.events.mother.event_mother import EventMother
from tests.sso.mothers.user_mother import UserMother
from tests.events.mocks.mock_event_repository import MockEventRepository
from tests.conversational_bot.mocks.mock_client import MockClient
from src.events.domain.event import Event
from src.events.use_cases.remember_use_case import RememberUseCase


def test_remember_use_case_execute():
    eventRepository = MockEventRepository()
    client = MockClient()
    useCase = RememberUseCase(eventRepository, client)
    events = [
        EventMother.withDelta(-10),  # SÍ avisa
        EventMother.withDelta(0, -3),  # SÍ avisa
        EventMother.withDelta(10),  # NO avisa
        EventMother.withDelta(0, 0, -8),  # SÍ avisa
        EventMother.withDelta(0, 4),  # NO avisa
        EventMother.withDelta(0, 0, 20),  # NO avisa
        EventMother.withDelta(0, 0, -45),  # SÍ avisa
        EventMother.withDelta(0, 0, 60),  # NO avisa
    ]
    for event in events:
        eventRepository.save(event)
    expected = 5

    pendingEvents = eventRepository.getPendingEvents(30)
    received = len(pendingEvents)

    assert received == expected


def test_remember_use_case_formatResponse():
    useCase = RememberUseCase(None, None)
    user = UserMother.getValid()
    event = Event(user, "RECORDAR_MEDICACION", {"medicamento": "rinialer"},
                  1654354871.0)
    expected = "RECORDAR_MEDICACION, 17:01: medicamento rinialer"

    received = useCase.formatResponse(event)

    assert received == expected
