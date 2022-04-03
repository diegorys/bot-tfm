import openai
from domain.response import Response


class Default:
    def __init__(self, intent):
        self.domain = 'basic'
        self.intent = intent

    def execute(self, user, request):
        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "

        openAIResponse = openai.Completion.create(
            engine="text-davinci-002",
            prompt="A partir de un texto aleatorio, el BOT dice que no entiende.\n\nHuman: Hablemos del tiempo\nAI: No estoy programado para hablar del tiempo\nHuman: ¿qué quieres comer?\nAI: Todavía no sé hablar de comida\nHuman: "
            + request
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )
        response = Response(user, openAIResponse["choices"][0]["text"]) 
        response.domain = self.domain
        response.intent = self.intent
        return response
