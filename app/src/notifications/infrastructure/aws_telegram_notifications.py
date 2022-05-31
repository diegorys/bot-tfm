try:
    import unzip_requirements
except ImportError:
    pass
import os
from src.language_models.dialogflow.dialogflow_language_model import DialogflowLanguageModel
from src.notifications.use_cases.send_notification_use_case import SendNotificationUseCase
from src.interfaces.telegram_client import TelegramClient
from src.conversational_bot.response_generator import ResponseGenerator
from src.sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def handle(event, context):
    text = event["message"]
    languageModel = DialogflowLanguageModel()
    responseGenerator: ResponseGenerator = ResponseGenerator(languageModel)
    usersRepository: DynamoDBUsersRepository = DynamoDBUsersRepository()
    client = TelegramClient(TELEGRAM_TOKEN)
    sendNotificationUseCase = SendNotificationUseCase(client, responseGenerator, usersRepository)
    sendNotificationUseCase.execute({"notification": text})
