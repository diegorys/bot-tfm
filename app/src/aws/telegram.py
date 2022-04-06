from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello

def handle(event, context):
    print('a')
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