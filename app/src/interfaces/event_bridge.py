import os
from src.events.use_cases.remember_use_case import RememberUseCase
from src.conversational_bot.client import Client
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository
from src.interfaces.telegram_client import TelegramClient


def handle(event, context):
    print("START")
    if not os.environ.get("TELEGRAM_TOKEN"):
        raise NotImplementedError

    eventRepository = DynamoDBEventRepository()
    telegramClient: Client = TelegramClient(os.environ.get("TELEGRAM_TOKEN"))
    useCase = RememberUseCase(eventRepository, telegramClient)
    useCase.execute(15)
    print("EXECUTED")
