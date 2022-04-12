try:
    import unzip_requirements
except ImportError:
    pass

from ast import Try
import os
import json
import openai
import telegram
from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello
from domain.dialog import Dialog
from domain.response import Response
from domain.user import User
from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
SERVICE_STATUS = os.environ.get("SERVICE_STATUS")

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps("ok"),
}

def handle(event, context):
    try:
        execute(event)
    except:
        print("Error!!!")
    finally: 
        return OK_RESPONSE

def execute(event):
    print(f"HANDLE TELEGRAM. SERVICE STATUS: {SERVICE_STATUS}")
    if not TELEGRAM_TOKEN:
        raise NotImplementedError

    bot = telegram.Bot(TELEGRAM_TOKEN)
    method = event.get("requestContext")["http"]["method"]
    if method == "POST" and event.get("body"):
        update = telegram.Update.de_json(json.loads(event.get("body")), bot)
        print(f"Message {update.message.message_id} received at {update.message.date}")
        print(event.get("body"))
        chat_id = update.message.chat.id
        text = update.message.text
        user = User(update.effective_chat.id, update.effective_chat.first_name)

        if text == "/start":
            nlu = GPT3NLU()
            nlu.handle(IntroduceOnself("/start"))
            response = nlu.executeCommand(user, "/start")
        elif not isServiceAvailable():
            response = generateUnavailableService(user)
        elif not hasCredits(user):
            response = generateNoCreditsText(user)
        else:
            response = getResponse(user, text)
        dialog = Dialog(
            update.message.message_id,
            user.id,
            user.name,
            text,
            response.domain,
            response.intent,
            response.command,
            response.text,
            str(update.message.date),
        )
        repository = DynamoDBDialogRepository()
        repository.save(dialog)
        bot.sendMessage(chat_id=chat_id, text=response.text)
        print("Message sent")


def getResponse(user, text):
    nlu = GPT3NLU()
    nlu.handle(Default("DESCONOCIDA"))
    nlu.handle(SayHello("SALUDAR"))
    nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
    nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))
    response = nlu.getResponse(user, text)
    print(text, response)
    return response

def isServiceAvailable():
    return int(SERVICE_STATUS) == 1

def generateUnavailableService(user):
    text = f"¡Gracias por colaborar en el experimento! Voy a registrar lo que me has escrito y te avisaré cuando esté activo para que podamos hablar."
    response = Response(user, text)
    return response

def hasCredits(user):
    return True

def generateNoCreditsText(user):
    text = f"Por limitaciones técnicas, no podemos hablar más por hoy. Mañana seguimos. Muchas gracias!"
    response = Response(user, text)
    return response
