import os
import math
import numpy as np
import openai
from domain.nlu import NLU

openai.api_key = os.getenv("OPENAI_API_KEY")


class GPT3(NLU):
    def classify(self, examples, request):
        prompt = examples + request + ":"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0,
            max_tokens=30,
            logprobs=5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"],
        )
        return response["choices"][0]["text"]

    def identifyDomain(self, knowledges, request):
        lines = ""
        for kn in knowledges:
            # lines += kn.text + ':|' + kn.domain + '|' + kn.intent + '|' + kn.entities + '|' + kn.response + '\n'
            lines += kn.text + ":" + kn.intent + "\n"
        return self.classify(lines, request + "."), 100

    # def identifyDomain(self, text):
    #     saludar = "Hola|SALUDAR\nHola, soy Diego|SALUDAR\nhola|SALUDAR\n¡Hola!|SALUDAR\n"
    #     medicina = (
    #         "Tengo que tomar un ibuprofeno los lunes|RECORDAR_MEDICINA\n"
    #         + "A las 12:00 me toca el paracetamol|RECORDAR_MEDICINA\n"
    #     )
    #     examples = saludar + medicina
    #     output = self.classify(examples, text + "|")
    #     # probs = output["choices"][0]["logprobs"]["token_logprobs"]
    #     # p = []
    #     # for prob in probs:
    #     #     p.append(round(math.exp(prob)*100, 2))
    #     # probability = round(np.mean(p), 2)
    #     probability = 100
    #     return output, probability

    def identifyEmotion(self, user, text):
        examples = (
            "tengo frío, hace frío:FRIO|medio|¿enciendo la calefacción?\n"
            + "Me siento bien:BIEN|medio|Me alegro\n"
            + "Me encuentro:MAL|medio|Anímate\n"
            + "Estoy solo:SOLO|medio|Yo estoy contigo\n"
            + "Un poco triste:TRISTE|medio|¿Por qué estás triste?\n"
            + "Aburrido:ABURRIDO|medio|¿Qué quieres hacer?\n"
            + "Contento:ALEGRE|medio|¡Qué bien que estés alegre!\n"
        )
        output = self.classify(examples, text)
        # probs = output["choices"][0]["logprobs"]["token_logprobs"]
        # p = []
        # for prob in probs:
        #     p.append(round(math.exp(prob)*100, 2))
        # probability = round(np.mean(p), 2)
        probability = 100
        outparts = output.split("|")
        probability = 100
        status = {
            "status": outparts[0],
            "log": output,
            "level": outparts[1],
            "probability": probability,
            "response": outparts[2],
        }
        return status
