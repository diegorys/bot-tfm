import json

from src.sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository
from src.applications.inactivity.use_cases.check_inactivity_use_case import CheckInactivityUseCase

usersRepository = DynamoDBUsersRepository()

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps("ok"),
}


def handle(event, context):
    try:
        useCase = CheckInactivityUseCase(usersRepository)
        useCase.execute()
    except Exception as e:
        print("Error!!!")
        print(e)
    finally:
        return OK_RESPONSE
