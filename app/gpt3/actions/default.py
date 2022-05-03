import os
# import openai
from conversational_bot.domain.response import Response

GPT3_ENGINE = os.environ["GPT3_ENGINE"]


class Default:
    def __init__(self, intent):
        self.domain = "basic"
        self.intent = intent

    def execute(self, user, request):
        # openAIResponse = openai.Completion.create(
        #     engine=GPT3_ENGINE,
        #     prompt="Human: Hablemos del tiempo\nAI: No estoy programado para hablar del tiempo\nHuman: ¿qué quieres comer?\nAI: Todavía no sé hablar de comida\nHuman: "
        #     + request
        #     + "\nAI:",
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0.6,
        #     stop=["Human:", "AI:"],
        # )
        # response = Response(user, openAIResponse["choices"][0]["text"]).strip()
        response = Response(user, "").strip()
        response.domain = self.domain
        response.intent = self.intent
        return response
