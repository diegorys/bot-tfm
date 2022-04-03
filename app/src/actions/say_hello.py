import openai

from domain.response import Response


class SayHello:
    def __init__(self, intent):
        self.domain = 'basic'
        self.intent = intent

    def execute(self, user, text):
        openAIResponse = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Conversación de saludo:\n\nHuman: Hola \nAI: Hola, encantando de saludarte.\nHuman: Hola, ¿quién eres?\nAI: Hola, soy tu asistente.\nHuman: Hola, ¿para qué sirves?\nAI: Hola, estoy aquí para cuidarte.\nHuman: Hola, ¿qué tal estás?\nAI: Hola, soy tu asistente. ¿Cómo estás?\nHuman: Hola, ¿quién eres?\nAI: Hola, soy tu cuidador. ¿En qué te puedo ayudar?\nHuman: Buenos días\nAI: Hola, ¿en qué te puedo ayudar?\nHuman: Buenas tardes\nAI: Buenas tardes, ¿qué tal estás?\nHuman: Buenas noches\nAI: Buenas noches\nHuman: "
            + text
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )

        response = Response(user, openAIResponse["choices"][0]["text"].replace("\n", ""))
        response.domain = self.domain
        response.intent = self.intent
        return response
