from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from notifications.use_cases.send_notification_use_case import SendNotificationUseCase
from conversational_bot.infrastructure.dummy.dummy_client import DummyClient
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


def test_send_notification():
    name = "Diego"
    user = User("diegorys", {"name": name})
    languageModel = DummyLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)

    frame: Frame = Frame("NOTIFICAR", user, "", {"notification": "Inicio"})
    client = DummyClient()
    sendNotificationUseCase = SendNotificationUseCase(client, responseGenerator)
    sendNotificationUseCase.execute(frame)
    assert client.dummyUser == user
    assert client.dummyText == "Inicio"
