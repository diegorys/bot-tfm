import json
import openai
import telegram
from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello
from domain.user import User
from infrastructure.gpt3.gpt3_nlu import GPT3NLU

openai.api_key = (
    "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"  # os.getenv("OPENAI_API_KEY")
)
# TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_TOKEN = "***REMOVED***"

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps("ok"),
}
nlu = GPT3NLU()

def handle(event, context):
    print('HANDLE TELEGRAM')
    if not TELEGRAM_TOKEN:
        raise NotImplementedError

    bot = telegram.Bot(TELEGRAM_TOKEN)
    method = event.get("requestContext")["http"]["method"]
    if method == "POST" and event.get("body"):
        print("Message received")
        print(event.get("body"))
        update = telegram.Update.de_json(json.loads(event.get("body")), bot)
        chat_id = update.message.chat.id
        text = update.message.text
        user = User(update.effective_chat.id, update.effective_chat.first_name)

        if text == "/start":
            response = nlu.executeCommand(user, "/start")
        else:
            response = getResponse(user, text)

        bot.sendMessage(chat_id=chat_id, text=response.text)
        print("Message sent")

        return OK_RESPONSE


def getResponse(user, text):
    nlu.handle(Default("DESCONOCIDA"))
    nlu.handle(SayHello("SALUDAR"))
    nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
    nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))
    nlu.handle(IntroduceOnself("/start"))
    response = nlu.getResponse(user, text)
    # self.log(text, response)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    return response
