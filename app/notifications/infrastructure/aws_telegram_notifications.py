try:
    import unzip_requirements
except ImportError:
    pass
import os
from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from notifications.use_cases.send_notification_use_case import SendNotificationUseCase
from conversational_bot.infrastructure.telegram.telegram_client import TelegramClient
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def handle(event, context):
    text = event["message"]
    languageModel = DummyLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    usersRepository: DynamoDBUsersRepository = DynamoDBUsersRepository()
    client = TelegramClient(TELEGRAM_TOKEN)
    sendNotificationUseCase = SendNotificationUseCase(client, responseGenerator, usersRepository)
    sendNotificationUseCase.execute({"notification": text})
