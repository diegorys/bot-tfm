from conversational_bot.domain.nlu import NLU
from conversational_bot.use_cases.process_message_use_case import ProcessMessageUseCase
from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from conversational_bot.infrastructure.dummy.dummy_client import DummyClient
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


def test_execute():
    name = "Diego"
    user = User("diegorys", {"name": name})
    client = DummyClient()
    languageModel = DummyLanguageModel()
    nlu: NLU = NLU(languageModel)
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    processMessageUseCase: ProcessMessageUseCase = ProcessMessageUseCase(nlu, responseGenerator)
    response = processMessageUseCase.execute(user, "Hola robot", "")
    client.emit(user, response)
    print("------------")
    print(client.dummyText)
    print("------------")
    possibleResponses = ["Hola", "¡Hola!", f"Hola {name}", "Hola, ¿qué tal?"]
    assert client.dummyText in possibleResponses
