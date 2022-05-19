from conversational_bot.reactive_bot import ReactiveBOT
from conversational_bot.domain.nlu import NLU
from conversational_bot.domain.command_manager import CommandManager
from conversational_bot.domain.dialog_manager import DialogManager
from conversational_bot.domain.response_generator import ResponseGenerator
from dialogflow.dialogflow_language_model import DialogflowLanguageModel

# from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel

def startConversationalBOT():
    import os
    from conversational_bot.infrastructure.telegram.telegram_bot import TelegramBot

    # languageModel = DummyLanguageModel()
    languageModel = DialogflowLanguageModel()
    nlu = NLU(languageModel)
    responseGenerator = ResponseGenerator(languageModel)
    dialogManager = DialogManager(languageModel)
    commandManager = CommandManager()
    bot = ReactiveBOT(
        nlu, dialogManager, responseGenerator, commandManager
    )
    print(f"STARTING CONVERSATIONAL BOT...")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    telegramBot: TelegramBot = TelegramBot(TELEGRAM_TOKEN, bot)
    print("WAITING FOR USER MESSAGE...")
    telegramBot.pool()


startConversationalBOT()
