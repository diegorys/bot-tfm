import os
import math
import numpy as np
import openai
from domain.nlu import NLU
from infrastructure.gpt3.gtp3 import GPT3

openai.api_key = os.getenv("OPENAI_API_KEY")


class GPT3NLU(NLU):
    def getResponse(self, request):
        gpt3 = GPT3()
        print("DOMINIO DE " + request)
        intent = gpt3.identifyIntent(request)
        print("IDENTIFICADA INTENCIÓN: " + intent)
        response = "No entiendo"
        if intent == "SALUDAR":
            response = gpt3.sayHello(request)
        elif intent == "REGISTRAR_MEDICACION":
            response = gpt3.addMedication(request)
        elif intent == "REGISTRAR_ESTADO":
            response = gpt3.addStatus(request)
        return intent, 100, response

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

    def identifyDomain(self, request):
        knowledges = self.knowledgeRepository.list()
        lines = ""
        for kn in knowledges:
            # lines += kn.text + ':|' + kn.domain + '|' + kn.intent + '|' + kn.entities + '|' + kn.response + '\n'
            lines += kn.text + ":" + kn.domain + "\n"
        return self.classify(lines, request + "."), 100

    def identifyIntent(self, domain, request):
        knowledges = self.knowledgeRepository.listDomain(domain)
        lines = ""
        for kn in knowledges:
            # lines += kn.text + ':|' + kn.domain + '|' + kn.intent + '|' + kn.entities + '|' + kn.response + '\n'
            lines += kn.text + ":" + kn.intent + "\n"
        return self.classify(lines, request + "."), 100

    def identifyResponse(self, intent, request):
        knowledges = self.knowledgeRepository.listIntent(intent)
        lines = ""
        for kn in knowledges:
            # lines += kn.text + ':|' + kn.domain + '|' + kn.intent + '|' + kn.entities + '|' + kn.response + '\n'
            lines += kn.text + ":" + kn.response + "\n"
        return self.classify(lines, request + "."), 100

    def generateText(self, request):
        knowledges = self.knowledgeRepository.list()
        lines = ""
        for kn in knowledges:
            lines += "Human: " + kn.text + "\n" + "AI: " + kn.response + "\n"
        return self.classify(lines, "Human: " + request + "\nAI: "), 100
