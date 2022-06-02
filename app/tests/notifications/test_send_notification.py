from src.notifications.use_cases.send_notification_use_case import SendNotificationUseCase
from src.conversational_bot.response_generator import ResponseGenerator
from tests.mock.mock_user_repository import MockUsersRepository
from tests.mock.mock_client import MockClient
from tests.mock.mock_language_model import MockLanguageModel


def test_send_notification():
    usersRepository = MockUsersRepository()
    languageModel = MockLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    client = MockClient()
    sendNotificationUseCase = SendNotificationUseCase(client, responseGenerator, usersRepository)
    sendNotificationUseCase.execute({"notification": "Inicio"})
    assert client.mockUser.username == usersRepository.list()[-1].username
    assert client.mockText == "Inicio"
    assert client.count == len(usersRepository.list())
