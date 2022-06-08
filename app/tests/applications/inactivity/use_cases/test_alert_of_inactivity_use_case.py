from src.applications.inactivity.use_cases.alert_of_inactivity_use_case import (
    AlertOfInactivityUseCase,
)
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother
from tests.conversational_bot.mocks.mock_client import MockClient


def test_execute():
    userRepository = MockUsersRepository()
    caregiver, dependent = UserMother.getPairCaregiverDependentWithNames("Cuidador", "Dependiente")
    dependent.markActive(False)
    userRepository.mockWith([caregiver, dependent])
    client: MockClient = MockClient()
    useCase = AlertOfInactivityUseCase(userRepository, client)
    expected = f"La persona a su cargo, {dependent.username} no responde."

    useCase.execute()
    received = client.mockText

    assert received == expected
