import os
# import openai
from domain.response import Response

GPT3_ENGINE = os.environ["GPT3_ENGINE"]


class SayHello:
    def __init__(self, intent):
        self.domain = "basic"
        self.intent = intent

    def execute(self, user, text):
        # openAIResponse = openai.Completion.create(
        #     engine=GPT3_ENGINE,
        #     prompt="Human: Hola \nAI: Hola, encantando de saludarte.\nHuman: Buenas tardes, ¿quién eres?\nAI: Buenas tardes, soy tu asistente.\nHuman: "
        #     + text
        #     + "\nAI:",
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0.6,
        #     stop=["Human:", "AI:"],
        # )

        # response = Response(user, openAIResponse["choices"][0]["text"].strip())
        response = Response(user, "hola")
        response.domain = self.domain
        response.intent = self.intent
        return response
