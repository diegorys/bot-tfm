from domain.response import Response

class IntroduceOnself:
    def __init__(self, intent):
        self.domain = 'basic'
        self.intent = intent

    def execute(self, user, text):
        response = Response(user, f"Hola {user.name}, soy tu cuidador, encantado de conocerte. Cuéntame cómo te sientes. También me puedes contar qué medicinas tomas. Y, si quieres, me puedes decir cuáles son tus fechas importantes y por qué. Todo lo que me escribas será almacenado en una base de datos para una revisión manual para mi TFM, así que no pongas nada que no quieras que lea. Para más información, escríbeme a diegorys@gmail.com. Gracias por colaborar.")
        response.domain = self.domain
        response.intent = self.intent
        return response
