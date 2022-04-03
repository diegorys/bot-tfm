import os
import math
import numpy as np
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class GPT3:
    def identifyIntent(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Lista de intenciones:\n\nSALUDAR, REGISTRAR_MEDICACION, DESCONOCIDA, REGISTRAR_ESTADO\n\nHola. Intención:SALUDAR\nTomar ibuprofeno. Intención:REGISTRAR_MEDICACION\nDigo algo por decir. Intención:DESCONOCIDA\nHey, qué tal?. Intención:SALUDAR\nEn un lugar de la mancha... Intención:DESCONOCIDA\nHola, buenas tardes, ¿quién eres?. Intención:SALUDAR\nMe siento triste. Intención:REGISTRAR_ESTADO\nEstoy alegre. Intención:REGISTRAR_ESTADO\n"
            + request
            + ". Intención:",
            temperature=0,
            max_tokens=10,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"],
        )

        return response["choices"][0]["text"]

    def sayHello(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Conversación de saludo:\n\nHuman: Hola \nAI: Hola, encantando de saludarte.\nHuman: Hola, ¿quién eres?\nAI: Hola, soy tu asistente.\nHuman: Hola, ¿para qué sirves?\nAI: Hola, estoy aquí para cuidarte.\nHuman: Hola, ¿qué tal estás?\nAI: Hola, soy tu asistente. ¿Cómo estás?\nHuman: Hola, ¿quién eres?\nAI: Hola, soy tu cuidador. ¿En qué te puedo ayudar?\nHuman: Buenos días\nAI: Hola, ¿en qué te puedo ayudar?\nHuman: Buenas tardes\nAI: Buenas tardes, ¿qué tal estás?\nHuman: Buenas noches\nAI: Buenas noches\nHuman: "
            + request
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )

        return response["choices"][0]["text"].replace("\n", "")

    def addMedication(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Convierte este texto a un comando:\nEjemplo: Recuérdame tomar el ibuprofeno el lunes a las 8\nComando: recordar-medicamento medicamento='ibuprofeno' hora='8:00' frecuencia='semanal' dia='lunes'\n\nEjemplo: Me toca tomar calcio a las 6 y media\nComando: recordar-medicamento medicamento='calcio' hora='18:30'\n\n"
            + request,
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )

        command = response["choices"][0]["text"].replace("\n", "")
        print("COMMAND MEDICATION ADDED: " + command)
        return self.responseMedicationAdded(command)

    def responseMedicationAdded(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="A partir de un comando de toma de medicamentos, se genera un texto para indicar al usuario que lo has entendido.\n\nCommand: recordar-medicamento medicamento='antihistamínico' hora='10:00'\nAI: Vale, me he apuntado que te tomas antihistamínico a las 10:00\nCommand: recordar-medicamento medicamento='ibuprofeno' hora='16:00'\nAI: De acuerdo, a las 16:00 te tomas el ibuprofeno\nCommand: "
            + request
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" AI:", "Command"],
        )
        return response["choices"][0]["text"]

    def addStatus(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Convierte este texto a un comando.\nEjemplo: Estoy solo\nComando: registrar-estado estado='soledad'\n\nEjemplo: Me siento triste\nComando: registrar-estado estado='tristeza'\n\nViva la alegría\n\nComando: registrar-estado estado='alegría'\n\n"
            + request,
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )

        command = response["choices"][0]["text"].replace("\n", "")
        print("COMMAND STATUS ADDED: " + command)
        # return command
        return self.responseStatusAdded(command)

    def responseStatusAdded(self, request):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="A partir de un comando de registro de estado, se genera un texto para responder al usuario.\n\nCommand: registrar-estado estado='tristeza'\nAI: Entiendo que estás triste, ¿qué puedo hacer por ti?\nCommand: registrar-estado estado='soledad'\nAI: Yo estoy contigo, no te preocupes\nCommand: registrar-estado estado='alegría'\nAI: ¡Qué bien que estés alegre!\nCommand: "
            + request
            + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" AI:", "Command"],
        )
        return response["choices"][0]["text"]