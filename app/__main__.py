import os
from src.conversational_bot.reactive_bot import ReactiveBOT
from src.conversational_bot.nlu import NLU
from src.conversational_bot.dialog_manager import DialogManager
from src.conversational_bot.response_generator import ResponseGenerator
from src.factories.command_manager_factory import CommandManagerFactory
from src.language_models.dialogflow.dialogflow_language_model import DialogflowLanguageModel
from src.interfaces.telegram_bot import TelegramBot
from src.storage.dynamodb_user_expression_repository import DynamoDBUserExpressionRepository


def startConversationalBOT():
    # languageModel = DummyLanguageModel()
    userExpressionRepository = DynamoDBUserExpressionRepository()
    languageModel = DialogflowLanguageModel()
    nlu = NLU(languageModel)
    responseGenerator = ResponseGenerator(languageModel)
    dialogManager = DialogManager(languageModel)
    commandManager = CommandManagerFactory.create()
    bot = ReactiveBOT(
        nlu, dialogManager, responseGenerator, commandManager, userExpressionRepository
    )
    print(f"STARTING CONVERSATIONAL BOT...")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    telegramBot: TelegramBot = TelegramBot(TELEGRAM_TOKEN, bot)
    print("WAITING FOR USER MESSAGE...")
    telegramBot.pool()


startConversationalBOT()
