from src.conversational_bot.response import Response
from src.applications.status.commands.ask_for_user_status_command import AskForUserStatusCommand
from src.applications.status.use_cases.ask_for_user_status_use_case import AskForUserStatusUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother

def test_ask_for_user_status_command_execute():
    repository = MockUsersRepository()
    useCase = AskForUserStatusUseCase(repository)
    command = AskForUserStatusCommand(useCase)
    user = UserMother.getValid()

    response = command.execute(user, {})

    assert type(response) is Response
