from tests.mock.dummy_user_expression_repository import DummyUsersExpressionRepository
from src.conversational_bot.command_manager import CommandManager
from src.conversational_bot.dialog_manager import DialogManager
from src.conversational_bot.nlu import NLU
from src.conversational_bot.reactive_bot import ReactiveBOT
from src.conversational_bot.response_generator import ResponseGenerator
from src.sso.domain.user import User
from tests.mock.dummy_language_model import DummyLanguageModel
from tests.mock.dummy_client import DummyClient


def test_execute():
    name = "Diego"
    user = User("diegorys", {"name": name})
    client = DummyClient()
    languageModel = DummyLanguageModel()
    userExpressionRepository = DummyUsersExpressionRepository()
    nlu: NLU = NLU(languageModel)
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    dialogManager = DialogManager(languageModel)
    commandManager = CommandManager()    
    bot = ReactiveBOT(
        nlu, dialogManager, responseGenerator, commandManager, userExpressionRepository
    )
    response = bot.execute(user, "Hola robot", "")
    client.emit(user, response.text)
    print("------------")
    print(client.dummyText)
    print("------------")
    possibleResponses = ["Hola", "¡Hola!", f"Hola {name}", "Hola, ¿qué tal?"]
    assert client.dummyText in possibleResponses
