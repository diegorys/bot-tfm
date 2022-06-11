from src.applications.inactivity.commands.register_activity_command import RegisterActivityCommand
from src.applications.inactivity.use_cases.register_activity_use_case import RegisterActivityUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother

def test_register_activity_command_execute():
    repository = MockUsersRepository()
    useCase = RegisterActivityUseCase(repository)
    command = RegisterActivityCommand(useCase)
    user = UserMother.getValid()

    response = command.execute(user, {})

    assert response is None
