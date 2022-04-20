from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello
from domain.dialog import Dialog
from domain.response import Response


class BOT:
    def __init__(self, nlu, config, repository=None):
        self.config = config
        self.nlu = nlu
        self.repository = repository
        self.nlu.handle(IntroduceOnself("/start"))
        self.nlu.handle(Default("DESCONOCIDA"))
        self.nlu.handle(SayHello("SALUDAR"))
        self.nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
        self.nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))

    def handleStart(self, text, user, id, date):
        response = self.nlu.executeCommand(user, "/start")
        self.log(text, user, id, date, response)
        return response

    def execute(self, text, user, id, date):
        print(f"Text: {text}")
        print(f"Service available? {self.config.SERVICE_AVAILABLE}")
        if self.config.SERVICE_AVAILABLE:
            response = self.getResponse(user, text)
        else:
            response = self.generateUnavailableService(user)
        self.log(text, user, id, date, response)
        return response

    def getResponse(self, user, text):
        response = self.nlu.getResponse(user, text)
        print(text, response)
        return response

    def generateUnavailableService(self, user):
        print("servicio no disponible")
        text = f"¡Gracias por colaborar en el experimento! Voy a registrar lo que me has escrito y te avisaré cuando esté activo para que podamos hablar."
        response = Response(user, text)
        return response

    def log(self, text, user, id, date, response):
        if self.repository:
            dialog = Dialog(
                id,
                user.id,
                user.name,
                text,
                response.domain,
                response.intent,
                response.command,
                response.text,
                date,
            )
            self.repository.save(dialog)
        else:
            print(
                id,
                user.id,
                user.name,
                text,
                response.domain,
                response.intent,
                response.command,
                response.text,
                date,
            )
