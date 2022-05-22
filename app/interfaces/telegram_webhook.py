try:
    import unzip_requirements
except ImportError:
    pass

import time
import os
import json
import telegram
from conversational_bot.user_expression import UserExpression
from sso.domain.user import User

# from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from storage.dynamodb_user_expression_repository import (
    DynamoDBUserExpressionRepository,
)
from conversational_bot.response import Response
from conversational_bot.dialog_manager import DialogManager
from conversational_bot.nlu import NLU
from conversational_bot.response_generator import ResponseGenerator
from factories.command_manager_factory import CommandManagerFactory
from language_models.dialogflow.dialogflow_language_model import (
    DialogflowLanguageModel,
)

# from language_models.dummy.dummy_language_model import DummyLanguageModel
from conversational_bot.reactive_bot import ReactiveBOT

repository = DynamoDBUserExpressionRepository()
SERVICE_STATUS = os.environ.get("SERVICE_STATUS") or 0

# languageModel = DummyLanguageModel()
languageModel = DialogflowLanguageModel()

nlu = NLU(languageModel)
responseGenerator = ResponseGenerator(languageModel)
dialogManager = DialogManager(languageModel)
commandManager = CommandManagerFactory.create()
reactiveBOT = ReactiveBOT(nlu, dialogManager, responseGenerator, commandManager)

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
    print(f"HANDLE TELEGRAM")
    if not os.environ.get("TELEGRAM_TOKEN"):
        raise NotImplementedError

    bot = telegram.Bot(os.environ.get("TELEGRAM_TOKEN"))
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
        date = str(update.message.date)
        response = botExecute(text, user, date)
        bot.sendMessage(chat_id=chat_id, text=response.text)
        print("Message sent")


def botExecute(text: str, user: User, date):
    print(f"Text: {text}")
    if text == "/start":
        print("/START")
        response = handleStart(user)
        log(text, user, date, response)
    else:
        response = reactiveBOT.execute(user, text, date)
        log(text, user, date, response)
    return response


def handleStart(user):
    message = (
        f"Hola {user.name}, soy tu cuidador"
        + ", encantado de conocerte. Si eres una persona mayor, cuéntame cómo te sientes.\n"
        + "También me puedes contar qué medicinas tomas. No necesito que sean reales.\n"
        + "Y, si quieres, me puedes decir cuáles son tus fechas importantes y por qué.\n"
        + "Tampoco necesito que sea verdad lo que me digas.\n\n"
        + "Si eres una persona joven, puedes preguntarme por la persona mayor a la que cuidas.\n\n"
        + "Todo lo que me escribas será almacenado en una base de datos para una revisión"
        + " manual para mi TFM, así que no pongas nada que no quieras que lea.\n"
        + "Por ahora el servicio de respuestas está desactivado y me limitaré a guardar"
        + " nuestras conversaciones.\n\n"
        + "Por favor, no sigas los consejos que te dé sin consultar antes a un experto, puesto"
        + " que sólo soy un BOT desarrollado para un TFM."
        + "\n\nPara más información, escribe a mi autor Diego a diegorys@gmail.com."
        + "\n\n¡Muchas gracias por colaborar!"
    )
    response = Response(
        user,
        message,
    )
    response.intent = "/start"
    return response


def log(text: str, user: User, date, response: Response):
    now = str(time.time())
    if repository:
        userExpression = UserExpression(
            now,
            user,
            text,
            response.intent,
            response.entities,
            response.text,
            date,
        )
        repository.save(userExpression)
    else:
        print(
            now,
            user,
            text,
            response.intent,
            response.entities,
            response.text,
            date,
        )
