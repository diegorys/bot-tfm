from conversational_bot.command_manager import CommandManager
from conversational_bot.dialog_manager import DialogManager
from conversational_bot.nlu import NLU
from conversational_bot.reactive_bot import ReactiveBOT
from conversational_bot.response_generator import ResponseGenerator
from sso.domain.user import User
from test.mock.dummy_language_model import DummyLanguageModel
from test.mock.dummy_client import DummyClient


def test_execute():
    name = "Diego"
    user = User("diegorys", {"name": name})
    client = DummyClient()
    languageModel = DummyLanguageModel()
    nlu: NLU = NLU(languageModel)
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    dialogManager = DialogManager(languageModel)
    commandManager = CommandManager()
    bot = ReactiveBOT(
        nlu, dialogManager, responseGenerator, commandManager
    )
    response = bot.execute(user, "Hola robot", "")
    client.emit(user, response.text)
    print("------------")
    print(client.dummyText)
    print("------------")
    possibleResponses = ["Hola", "¡Hola!", f"Hola {name}", "Hola, ¿qué tal?"]
    assert client.dummyText in possibleResponses
