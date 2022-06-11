from src.applications.status.commands.register_user_status_command import RegisterUserStatusCommand
from src.applications.status.use_cases.register_user_status_use_case import RegisterUserStatusUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother
from tests.conversational_bot.mocks.mock_client import MockClient

def test_register_user_status_command_execute():
    repository = MockUsersRepository()
    client = MockClient()
    useCase = RegisterUserStatusUseCase(repository, client)
    command = RegisterUserStatusCommand(useCase)
    user = UserMother.getValid()

    response = command.execute(user, {"estado": "bien"})

    assert response is None
