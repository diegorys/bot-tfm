from notifications.use_cases.send_notification_use_case import SendNotificationUseCase
from conversational_bot.response_generator import ResponseGenerator
from test.mock.dummy_user_repository import DummyUsersRepository
from test.mock.dummy_client import DummyClient
from test.mock.dummy_language_model import DummyLanguageModel


def test_send_notification():
    usersRepository = DummyUsersRepository()
    languageModel = DummyLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    client = DummyClient()
    sendNotificationUseCase = SendNotificationUseCase(client, responseGenerator, usersRepository)
    sendNotificationUseCase.execute({"notification": "Inicio"})
    assert client.dummyUser.username == usersRepository.list()[-1].username
    assert client.dummyText == "Inicio"
    assert client.count == len(usersRepository.list())
