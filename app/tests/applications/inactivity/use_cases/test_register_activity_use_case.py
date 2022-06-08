from src.applications.inactivity.use_cases.register_activity_use_case import RegisterActivityUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother


def test_register_activity_use_case():
    userRepository = MockUsersRepository()
    user = UserMother.getValid()

    useCase = RegisterActivityUseCase(userRepository)
    useCase.execute(user)

    assert user.isActive()
