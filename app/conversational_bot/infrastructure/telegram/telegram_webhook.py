try:
    import unzip_requirements
except ImportError:
    pass

import os
import json
import telegram
from domain.bot import BOT
from conversational_bot.domain.response import Response
from sso.domain.user import User
# from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository
from infrastructure.configuration import Config
from conversational_bot.domain.nlu import NLU
from conversational_bot.domain.response_generator import ResponseGenerator
from conversational_bot.infrastructure.dummy.dummy_language_model import DummyLanguageModel
from conversational_bot.use_cases.process_message_use_case import ProcessMessageUseCase

config = Config()
gpt3NLU = None #GPT3NLU()
repository = DynamoDBDialogRepository()
bot = BOT(gpt3NLU, config, repository)
available = config.SERVICE_AVAILABLE

languageModel = DummyLanguageModel()
nlu = NLU(languageModel)
responseGenerator = ResponseGenerator(languageModel)
processMessageUseCase = ProcessMessageUseCase(nlu, responseGenerator)

if "TELEGRAM_UPDATE_ID" not in os.environ.keys():
    os.environ["TELEGRAM_UPDATE_ID"] = ""
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
        idempotency = str(update.update_id) + "_" + str(update.effective_chat.id)
        print(f"Check idempotency with {idempotency}")
        print(pendingIdempotency)
        oldIdempotency = os.environ["TELEGRAM_UPDATE_ID"]
        print(f"Last message: {oldIdempotency}")
        if os.environ["TELEGRAM_UPDATE_ID"] == idempotency:
            raise Exception(f"Update ID duplicated: {idempotency}")
        os.environ["TELEGRAM_UPDATE_ID"] = idempotency
        if idempotency in pendingIdempotency:
            raise Exception(f"Idempotency duplicated: {idempotency}")
        pendingIdempotency.append(idempotency)
        print(f"Message {update.update_id} received at {update.message.date}")
        print(event.get("body"))
        chat_id = update.message.chat.id
        text = update.message.text
        user = User(
            update.effective_chat.first_name,
            {"telegram_id": update.effective_chat.id, "name": update.effective_chat.first_name},
        )
        id = update.update_id
        date = str(update.message.date)
        response = botExecute(text, user, available, id, date)
        bot.sendMessage(chat_id=chat_id, text=response.text)
        print("Message sent")


def botExecute(text: str, user: User, available, id, date):
    print(f"Text: {text}")
    print(f"Service available? {available}")
    if text == "/start":
        print("/START")
        response = bot.handleStart(text, user, id, date)
    else:
        txt = processMessageUseCase.execute(user, text, date)
        response: Response = Response(user, txt)
        bot.log(text, user, id, date, response)
    return response
