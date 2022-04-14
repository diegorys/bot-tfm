try:
    import unzip_requirements
except ImportError:
    pass

import json

import telegram
from domain.bot import BOT
from domain.user import User
from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository
from infrastructure.configuration import Config

config = Config()
nlu = GPT3NLU()
repository = DynamoDBDialogRepository()
bot = BOT(nlu, config, repository)

pendingIdempotency = []

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps("ok"),
}


def handle(event, context):
    try:
        execute(event)
    except Exception as e:
        print("Error!!!")
        print(e)
    finally:
        return OK_RESPONSE


def execute(event):
    print(f"HANDLE TELEGRAM. SERVICE STATUS: {available}")
    if not config.TELEGRAM_TOKEN:
        raise NotImplementedError

    bot = telegram.Bot(config.TELEGRAM_TOKEN)
    method = event.get("requestContext")["http"]["method"]
    if method == "POST" and event.get("body"):
        update = telegram.Update.de_json(json.loads(event.get("body")), bot)
        idempotency = str(update.message.message_id) + "_" + str(update.effective_chat.id)
        print(f"Check idempotency with {idempotency}")
        print(pendingIdempotency)
        if idempotency in pendingIdempotency:
            raise Exception(f"Duplicated: {idempotency}")
        pendingIdempotency.append(idempotency)
        print(f"Message {update.message.message_id} received at {update.message.date}")
        print(event.get("body"))
        chat_id = update.message.chat.id
        text = update.message.text
        user = User(update.effective_chat.id, update.effective_chat.first_name)
        available = config.SERVICE_AVAILABLE
        id = update.message.message_id
        date = str(update.message.date)
        response = botExecute(text, user, available, id, date)
        bot.sendMessage(chat_id=chat_id, text=response.text)
        print("Message sent")


def botExecute(text, user, available, id, date):
    print(f"Text: {text}")
    print(f"Service available? {available}")
    if text == "/start":
        print("/START")
        response = bot.handleStart(user)
    else:
        response = bot.execute(text, user, id, date)
    return response