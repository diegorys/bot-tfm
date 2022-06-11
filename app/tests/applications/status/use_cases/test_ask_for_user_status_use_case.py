from datetime import datetime, timedelta
from src.applications.status.domain.user_in_status import UserInStatus
from src.conversational_bot.response import Response
from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase
from tests.applications.status.mocks.mock_user_in_status_repository import (
    MockUserInStatusRepository,
)
from tests.applications.status.mother.user_in_status_mother import UserInStatusMother
from tests.sso.mothers.user_mother import UserMother


def test_ask_for_user_status_execute_no_dependents():
    repository = MockUserInStatusRepository()
    useCase = AskForUserStatusUseCase(repository)
    user = UserMother.getValid()
    expected: str = "No tienes a nadie a tu cuidado."

    received = useCase.execute(user)

    assert received.text == expected


def test_ask_for_user_status_execute_with_dependents_unknown_state():
    repository = MockUserInStatusRepository()
    useCase = AskForUserStatusUseCase(repository)
    caregiver = UserMother.forId("a")
    dependent = UserMother.forId("b")
    caregiver.addDependent(dependent)
    expected: str = f"Desconozco el estado de {dependent.username}."

    received = useCase.execute(caregiver)

    assert received.text == expected


def test_ask_for_user_status_execute_with_dependents_unknown_state():
    repository = MockUserInStatusRepository()
    useCase = AskForUserStatusUseCase(repository)
    caregiver = UserMother.forId("a")
    userInStatus: UserInStatus = UserInStatusMother.forStatusNow("bien")
    dependent = userInStatus.user
    dependent.id = "b"
    caregiver.addDependent(dependent)
    repository.save(userInStatus)
    dt_object = datetime.fromtimestamp(userInStatus.timestamp)
    date = (dt_object + timedelta(hours=2)).strftime("%d-%m-%Y a las %H:%M:%S")
    expected: str = f"El estado de {userInStatus.user.username} el {date} era de {userInStatus.status.name}."

    received = useCase.execute(caregiver)

    assert received.text == expected
