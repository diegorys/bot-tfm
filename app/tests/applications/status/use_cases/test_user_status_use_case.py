from src.applications.status.use_cases.register_user_status_use_case import (
    RegisterUserStatusUseCase,
)
from tests.applications.status.mother.user_in_status_mother import UserInStatusMother
from tests.applications.status.mocks.mock_user_in_status_repository import (
    MockUserInStatusRepository,
)
from src.conversational_bot.client import Client
from tests.conversational_bot.mocks.mock_client import MockClient
from tests.sso.mothers.user_mother import UserMother


def test_register_use_case_execute_negative_status():
    repository = MockUserInStatusRepository()
    client = MockClient()
    useCase = RegisterUserStatusUseCase(repository, client)
    badStatus = useCase.blackList[0]
    userInStatus = UserInStatusMother.forStatusNow(badStatus)
    caregiver = UserMother.getValid("caregiver")
    userInStatus.user.setCaregiver(caregiver)
    expected = f"Hola {caregiver.username}, el estado de la persona a la que cuidas, {userInStatus.user.username}, es de {userInStatus.status.name}"

    useCase.execute(userInStatus)
    received = client.mockText

    assert received == expected
