from random import randrange
import time
from sso.domain.user import User
# from actions.default import Default
# from actions.introduce_oneself import IntroduceOnself
# from actions.register_medicine import RegisterMedicine
# from actions.register_status import RegisterStatus
# from actions.say_hello import SayHello
from domain.dialog import Dialog
from conversational_bot.domain.response import Response


class BOT:
    def __init__(self, nlu, config, repository=None):
        self.config = config
        self.nlu = nlu
        self.repository = repository
        # self.nlu.handle(IntroduceOnself("/start"))
        # self.nlu.handle(Default("DESCONOCIDA"))
        # self.nlu.handle(SayHello("SALUDAR"))
        # self.nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
        # self.nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))

    def handleStart(self, text, user, id, date):
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
        response.domain = self.domain
        response.intent = self.intent
        self.log(text, user, id, date, response)
        return response

    def generateUnavailableService(self, user):
        print("servicio no disponible")
        phrases = [
            "¡Tomo nota!",
            "Me lo apunto",
            "Queda anotado",
            "Anotado",
            "¿Qué más quieres contarme?",
            "Cuéntame más cosas",
            "Me interesa todo lo que me digas",
        ]
        index = randrange(0, len(phrases))
        # text = f"¡Gracias por colaborar en el experimento! Voy a registrar lo que me has escrito y te avisaré cuando esté activo para que podamos hablar."
        text = phrases[index]
        response = Response(user, text)
        return response

    def log(self, text, user: User, id, date, response):
        now = str(time.time())
        if self.repository:
            dialog = Dialog(
                now,
                user.metadata["telegram_id"],
                user.username,
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
                user.metadata["telegram_id"],
                user.username,
                text,
                response.domain,
                response.intent,
                response.command,
                response.text,
                date,
            )
