import os
from src.conversational_bot.frame import Frame
from src.events.domain.event import Event
from src.conversational_bot.client import Client
from src.conversational_bot.language_model import LanguageModel
from src.conversational_bot.response_generator import ResponseGenerator
from src.conversational_bot.proactive_bot import ProactiveBOT
from src.language_models.dialogflow.dialogflow_language_model import DialogflowLanguageModel
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository
from src.interfaces.telegram_client import TelegramClient


def handle(event, context):
    if not os.environ.get("TELEGRAM_TOKEN"):
        raise NotImplementedError

    eventRepository = DynamoDBEventRepository()
    events = eventRepository.getPendingEvents()
    languageModel: LanguageModel = DialogflowLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    telegramClient: Client = TelegramClient(os.environ.get("TELEGRAM_TOKEN"))
    bot: ProactiveBOT = ProactiveBOT(responseGenerator, telegramClient)
    for event in events:
        event: Event = event
        if event.hasToBeNotified():
            frame: Frame = Frame(event.name, event.user, "", event.entities)
            bot.execute(frame)
            eventRepository.markAsNotified(event)
