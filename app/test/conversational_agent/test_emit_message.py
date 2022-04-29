from conversational_bot.use_cases.emit_message_use_case import EmitMessageUseCase
from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from conversational_bot.infrastructure.dummy.dummy_client import DummyClient
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


def test_execute():
    name = "Diego"
    user = User("diegorys", {"name": name})
    frame: Frame = Frame("SALUDAR", user, "Hola robot")
    client = DummyClient()
    languageModel = DummyLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(client, languageModel)
    emitMessageUseCase: EmitMessageUseCase = EmitMessageUseCase(responseGenerator)
    emitMessageUseCase.execute(frame)
    print("------------")
    print(client.dummyText)
    print("------------")
    possibleResponses = ["Hola", "¡Hola!", f"Hola {name}" "Hola, ¿qué tal?"]
    assert client.dummyText in possibleResponses
