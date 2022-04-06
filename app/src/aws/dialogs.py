import json
from domain.dialog import Dialog

# from infrastructure.sqlite3.sqlite3_dialog_repository import SQLite3DialogRepository
# from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository


def handle(event, context):
    # dialogRepository = SQLite3DialogRepository("bot-tfm")
    # dialogs = dialogRepository.list()
    dialogs = [Dialog(1, "pepe", "Hola", "basic", "saludar", "", "Hola pepe", "")]
    r = []
    for dialog in dialogs:
        r.append(
            {
                "date": dialog.date,
                "text": dialog.text,
                "response": dialog.response,
                "username": dialog.username,
                "domain": dialog.domain,
                "intent": dialog.intent,
            }
        )
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(r),
    }
    return response
