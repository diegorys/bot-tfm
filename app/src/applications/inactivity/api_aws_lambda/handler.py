import os
import json

from src.sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository
from src.applications.inactivity.use_cases.check_inactivity_use_case import CheckInactivityUseCase
from src.interfaces.telegram_client import TelegramClient

usersRepository = DynamoDBUsersRepository()

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps("ok"),
}


def handle(event, context):
    print("-----------------------------")
    try:
        print("TESTING INACTIVITY HANDLER")
        if not os.environ.get("TELEGRAM_TOKEN"):
            raise NotImplementedError
        telegramClient = TelegramClient(os.environ.get("TELEGRAM_TOKEN"))
        useCase = CheckInactivityUseCase(usersRepository, telegramClient)
        useCase.execute()
    except Exception as e:
        print("Error!!!")
        print(e)
    finally:
        print("-----------------------------")
        return OK_RESPONSE
