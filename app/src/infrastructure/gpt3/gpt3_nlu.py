import os
import numpy as np
import openai
from domain.nlu import NLU

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT3_ENGINE = os.environ["GPT3_ENGINE"]


class GPT3NLU(NLU):
    def identifyIntent(self, request):
        response = openai.Completion.create(
            engine=GPT3_ENGINE,
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
