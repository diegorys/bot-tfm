from src.applications.inactivity.use_cases.check_inactivity_use_case import CheckInactivityUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother
from tests.conversational_bot.mocks.mock_client import MockClient


def test_check_inactivity_use_case_active_marked_active():
    userRepository = MockUsersRepository()
    client: MockClient = MockClient()
    # dependantA is active and marked as active.
    caregiverA, dependantA = UserMother.getPairCaregiverDependentWithNames(
        "Cuidador A", "Dependiente A"
    )
    dependantA.registerActivity()
    dependantA.markActive(True)
    userRepository.mockWith([caregiverA, dependantA])

    useCase = CheckInactivityUseCase(userRepository, client)
    useCase.execute()

    received = client.mockText
    expected = ""

    assert dependantA.isMarkedAsActive() is True
    assert received == expected


def test_check_inactivity_use_case_active_marked_inactive():
    userRepository = MockUsersRepository()
    client: MockClient = MockClient()
    # dependantB is active and marked as inactive.
    caregiverB, dependantB = UserMother.getPairCaregiverDependentWithNames(
        "Cuidador B", "Dependiente B"
    )
    dependantB.registerActivity()
    dependantB.markActive(False)
    userRepository.mockWith(
        [
            caregiverB,
            dependantB,
        ]
    )
    useCase = CheckInactivityUseCase(userRepository, client)
    useCase.execute()
    received = client.mockText
    expected = f"La persona a su cargo, {dependantB.username}, no responde."

    assert dependantB.isMarkedAsActive() is False
    assert received == expected


def test_check_inactivity_use_case_inactive_marked_active():
    userRepository = MockUsersRepository()
    client: MockClient = MockClient()

    # dependantC is inactive and marked as active.
    caregiverC, dependantC = UserMother.getPairCaregiverDependentWithNames(
        "Cuidador C", "Dependiente C"
    )
    dependantC.markActive(True)

    userRepository.mockWith(
        [
            caregiverC,
            dependantC,
        ]
    )
    useCase = CheckInactivityUseCase(userRepository, client)
    useCase.execute()
    received = client.mockText
    expected = f"Hola {dependantC.username}, hace un rato que no hablamos, ¿cómo estás?"

    assert dependantC.isMarkedAsActive() is False
    assert received == expected


def test_check_inactivity_use_case_inactive_marked_inactive():
    userRepository = MockUsersRepository()
    client: MockClient = MockClient()
    # dependantD is inactive and marked as inactive.
    caregiverD, dependantD = UserMother.getPairCaregiverDependentWithNames(
        "Cuidador D", "Dependiente D"
    )
    dependantD.markActive(False)
    userRepository.mockWith(
        [
            caregiverD,
            dependantD,
        ]
    )
    useCase = CheckInactivityUseCase(userRepository, client)
    useCase.execute()
    received = client.mockText
    expected = f"La persona a su cargo, {dependantD.username}, no responde."

    assert dependantD.isMarkedAsActive() is False
    assert received == expected
