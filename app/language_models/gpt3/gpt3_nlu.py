# import openai
from conversational_bot.frame import Frame
from conversational_bot.language_model import LanguageModel

# openai.api_key = os.getenv("OPENAI_API_KEY")
# GPT3_ENGINE = os.environ["GPT3_ENGINE"]


class GPT3NLU(LanguageModel):
    def identifyIntent(self, text: str):
        prompt = (
            "Ej: Hola.\nIntent: SALUDAR\nEj: Buenas tardes.\nIntent: SALUDAR\nEj: Tomar ibuprofeno.\nIntent: REGISTRAR_MEDICACION\nEj: Digo algo por decir.\nIntent: DESCONOCIDA\nEj: Me siento triste.\nIntent: REGISTRAR_ESTADO\nEj: "
            + text
            + ".\nIntent:"
        )
        print("IDENTIFICAR INTENCIÓN!!!")
        print(prompt)
        # response = openai.Completion.create(
        #     engine=GPT3_ENGINE,
        #     prompt=prompt,
        #     temperature=0,
        #     max_tokens=10,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0,
        #     stop=["Ej:", "Intent:"],
        # )

        # return response["choices"][0]["text"].strip()
        return ""

        pass

    def generateText(self, frame: Frame) -> str:
        pass
