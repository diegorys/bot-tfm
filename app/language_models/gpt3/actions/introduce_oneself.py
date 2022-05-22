from conversational_bot.response import Response


class IntroduceOnself:
    def __init__(self, intent):
        self.domain = "basic"
        self.intent = intent

    def execute(self, user, text):
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
        return response
