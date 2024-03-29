from random import randrange
from src.conversational_bot.frame import Frame
from src.conversational_bot.language_model import LanguageModel


class DummyLanguageModel(LanguageModel):
    def identifyIntent(self, text: str) -> str:
        intent: str = "DESCONOCIDO"
        if "hola" in text.lower():
            intent = "SALUDAR"
        if "medicina" in text.lower() or "medicamento" in text.lower():
            intent = "REGISTRAR_MEDICAMENTO"
        if "adiós" in text.lower():
            intent = "DESPEDIRSE"
        return intent, {}

    def generateRequireParametersText(self, frame: Frame) -> str:
        response = ""
        for entity in frame.entities.keys():
            value = frame.entities[entity]
            if not value:
                response = f"required {entity}"
                break
        return response

    def generateText(self, frame: Frame) -> str:
        response = ""
        if "SALUDAR" == frame.intent:
            response = self.generateSaludarResponse(frame)
        elif "DESPEDIRSE" == frame.intent:
            response = self.generateDespedidaResponse(frame)
        elif "REGISTRAR_MEDICAMENTO" == frame.intent:
            response = self.generateRegisterMedicationResponse(frame)
        elif "DESCONOCIDO" == frame.intent:
            response = self.generateUnderstandResponse(frame)
        elif "NOTIFICATION" == frame.intent:
            response = self.generateNotificationResponse(frame)
        else:
            response = self.generateUnderstandResponse(frame)
        return response

    def generateSaludarResponse(self, frame):
        return self.generateRandomResponse(
            ["Hola", "¡Hola!", f"Hola {frame.user.metadata['name']}", "Hola, ¿qué tal?"]
        )

    def generateDespedidaResponse(self, frame):
        return self.generateRandomResponse(
            ["Hasta luego", "¡Nos vemos!", f"Hablamos luego, {frame.user.metadata['name']}"]
        )

    def generateRegisterMedicationResponse(self, frame):
        return self.generateRandomResponse(
            [
                "Registro la medicina",
                "Tomo nota de que te tienes que tomar la medicina",
                f"Me apunto el medicamento, {frame.user.metadata['name']}",
            ]
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
                # f'No estoy programado para "{frame.intent}", pero lo apunto',
                # f'Todavía tengo que aprender a "{frame.intent}", pero tomo nota',
            ]
        )

    def generateNotUnderstandResponse(self, frame):
        return self.generateRandomResponse(
            ["No te entiendo", "No sé qué dices", f"No estoy programado para {frame.intent}"]
        )

    def generateNotificationResponse(self, frame: Frame):
        notification = frame.entities["notification"].replace("<username>", frame.user.username)
        return notification

    def generateRandomResponse(self, phrases):
        index = randrange(0, len(phrases))
        return phrases[index]
