import json
import telegram

from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello

OK_RESPONSE = {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps('ok')
}

def handle(event, context):
    # TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    TELEGRAM_TOKEN = "***REMOVED***"
    if not TELEGRAM_TOKEN:
        raise NotImplementedError

    bot = telegram.Bot(TELEGRAM_TOKEN)
    if event.get('httpMethod') == 'POST' and event.get('body'): 
        print('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == '/start':
            text = """Hello, human! I am an echo bot, built with Python and the Serverless Framework.
            You can take a look at my source code here: https://github.com/jonatasbaldin/serverless-telegram-bot.
            If you have any issues, please drop a tweet to my creator: https://twitter.com/jonatsbaldin. Happy botting!"""

        bot.sendMessage(chat_id=chat_id, text=text)
        print('Message sent')

        return OK_RESPONSE

def getResponse(user, text):
    nlu = GPT3NLU()
    nlu.handle(Default("DESCONOCIDA"))
    nlu.handle(SayHello("SALUDAR"))
    nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
    nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))
    nlu.handle(IntroduceOnself("/start"))
    # response = nlu.getResponse(user, text)
    # self.log(text, response)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    return "vale"