from conversational_bot.domain.nlu import NLU
from conversational_bot.domain.response_generator import ResponseGenerator
from dialogflow.domain.dialogflow_language_model import DialogflowLanguageModel
# from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from conversational_bot.use_cases.process_message_use_case import ProcessMessageUseCase


def startConversationalBOT():
    import os
    from conversational_bot.infrastructure.telegram.telegram_bot import TelegramBot

    # languageModel = DummyLanguageModel()
    languageModel = DialogflowLanguageModel()
    nlu = NLU(languageModel)
    responseGenerator = ResponseGenerator(languageModel)
    processMessageUseCase = ProcessMessageUseCase(nlu, responseGenerator)
    print(f"STARTING CONVERSATIONAL BOT...")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    telegramBot: TelegramBot = TelegramBot(TELEGRAM_TOKEN, processMessageUseCase)
    print("WAITING FOR USER MESSAGE...")
    telegramBot.pool()


startConversationalBOT()
