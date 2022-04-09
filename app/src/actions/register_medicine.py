import os
import openai
from domain.response import Response

GPT3_ENGINE = os.environ["GPT3_ENGINE"]

class RegisterMedicine:
    def __init__(self, intent):
        self.domain = 'medicine'
        self.intent = intent

    def execute(self, user, text):
        openAIResponse = openai.Completion.create(
            engine=GPT3_ENGINE,
            prompt="Ej: Recuérdame tomar el ibuprofeno el lunes a las 8\nCommand: recordar-medicamento medicamento='ibuprofeno' hora='8:00' frecuencia='semanal' dia='lunes'\nEj: Me toca tomar calcio a las 6 y media\nCommand: recordar-medicamento medicamento='calcio' hora='18:30'\nEj: "
            + text
            + ".\nCommand:",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
            stop=["Ej:", "Command:"]
        )

        command = openAIResponse["choices"][0]["text"].strip()
        print("COMMAND MEDICATION ADDED: " + command)
        response = Response(user, self.responseMedicationAdded(command))
        response.domain = self.domain
        response.intent = self.intent
        response.command = command
        return response

    def responseMedicationAdded(self, request):
        response = openai.Completion.create(
            engine=GPT3_ENGINE,
            prompt="Command: recordar-medicamento medicamento='antihistamínico' hora='10:00'\nAI: Vale, me he apuntado que te tomas antihistamínico a las 10:00\nCommand: recordar-medicamento medicamento='ibuprofeno' hora='16:00'\nAI: De acuerdo, a las 16:00 te tomas el ibuprofeno\nCommand: "
            + request
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["AI:", "Command:"],
        )
        return response["choices"][0]["text"].strip()
