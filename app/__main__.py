import os
from conversational_bot.reactive_bot import ReactiveBOT
from conversational_bot.nlu import NLU
from conversational_bot.dialog_manager import DialogManager
from conversational_bot.response_generator import ResponseGenerator
from factories.command_manager_factory import CommandManagerFactory
from language_models.dialogflow.dialogflow_language_model import DialogflowLanguageModel
from interfaces.telegram_bot import TelegramBot

def startConversationalBOT():
    # languageModel = DummyLanguageModel()
    languageModel = DialogflowLanguageModel()
    nlu = NLU(languageModel)
    responseGenerator = ResponseGenerator(languageModel)
    dialogManager = DialogManager(languageModel)
    commandManager = CommandManagerFactory.create()
    bot = ReactiveBOT(
        nlu, dialogManager, responseGenerator, commandManager
    )
    print(f"STARTING CONVERSATIONAL BOT...")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    telegramBot: TelegramBot = TelegramBot(TELEGRAM_TOKEN, bot)
    print("WAITING FOR USER MESSAGE...")
    telegramBot.pool()


startConversationalBOT()
