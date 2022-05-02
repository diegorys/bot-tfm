from random import randrange
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.language_model import LanguageModel


class DummyLanguageModel(LanguageModel):
    def identifyIntent(self, text: str) -> str:
        intent: str = "DESCONOCIDO"
        if "hola" in text.lower():
            intent = "SALUDAR"
        if "adiós" in text.lower():
            intent = "DESPEDIRSE"
        return intent, {}

    def generateText(self, frame: Frame) -> str:
        response = ""
        if "SALUDAR" == frame.intent:
            response = self.generateSaludarResponse(frame)
        elif "DESPEDIRSE" == frame.intent:
            response = self.generateDespedidaResponse(frame)
        elif "DESCONOCIDO" == frame.intent:
            response = self.generateNotUnderstandResponse(frame)
        else:
            response = self.generateNotUnderstandResponse(frame)
        print(f"Response {response}")
        return response

    def generateSaludarResponse(self, frame):
        return self.generateRandomResponse(
            ["Hola", "¡Hola!", f"Hola {frame.user.metadata['name']}", "Hola, ¿qué tal?"]
        )

    def generateDespedidaResponse(self, frame):
        return self.generateRandomResponse(
            ["Hasta luego", "¡Nos vemos!", f"Hablamos luego, {frame.user.metadata['name']}"]
        )

    def generateUnderstandResponse(self, frame):
        return self.generateRandomResponse(
            [
                "¡Tomo nota!",
                "Me lo apunto",
                "Queda anotado",
                "Anotado",
                "¿Qué más quieres contarme?",
                "Cuéntame más cosas",
                "Me interesa todo lo que me digas",
                f'No estoy programado para "{frame.intent}", pero lo apunto',
                f'Todavía tengo que aprender a "{frame.intent}", pero tomo nota',
            ]
        )

    def generateNotUnderstandResponse(self, frame):
        return self.generateRandomResponse(
            ["No te entiendo", "No sé qué dices", f"No estoy programado para {frame.intent}"]
        )

    def generateRandomResponse(self, phrases):
        index = randrange(0, len(phrases))
        return phrases[index]
