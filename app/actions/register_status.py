import os
# import openai
from domain.response import Response

GPT3_ENGINE = os.environ["GPT3_ENGINE"]


class RegisterStatus:
    def __init__(self, intent):
        self.domain = "status"
        self.intent = intent

    def execute(self, user, text):
        # openAIResponse = openai.Completion.create(
        #     engine=GPT3_ENGINE,
        #     prompt="Ej: Estoy solo\nCommand: registrar-estado estado='soledad'\nEj: Me siento triste\nComando: registrar-estado estado='tristeza'\nEj: "
        #     + text
        #     + ".\nCommand:",
        #     temperature=0,
        #     max_tokens=100,
        #     top_p=1,
        #     frequency_penalty=0.2,
        #     presence_penalty=0,
        #     stop=["Ej:", "Command:"],
        # )

        # command = openAIResponse["choices"][0]["text"].strip()
        # print("COMMAND STATUS ADDED: " + command)
        command = ""
        response = Response(user, self.responseStatusAdded(command))
        response.domain = self.domain
        response.intent = self.intent
        response.command = command
        return response

    def responseStatusAdded(self, request):
        # response = openai.Completion.create(
        #     engine=GPT3_ENGINE,
        #     prompt="Command: registrar-estado estado='tristeza'\nAI: ¿Qué puedo hacer por ti?\nCommand: registrar-estado estado='soledad'\nAI: Estoy contigo, no te preocupes\nCommand: registrar-estado estado='alegría'\nAI: ¡Qué bien que estés alegre!\nCommand: "
        #     + request
        #     + "\nAI:",
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0.6,
        #     stop=["AI:", "Command:"]
        # )
        # return response["choices"][0]["text"].strip()
        return ""
