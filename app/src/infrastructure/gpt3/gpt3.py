import os
import openai
from domain.nlu import NLU

openai.api_key = os.getenv("OPENAI_API_KEY")

class GPT3(NLU):

  def classify(self, examples, request):
      prompt = examples + "\n" + request + ":"
      response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0,
        max_tokens=30,
        logprobs=5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
      )
      return response["choices"][0]["text"]
  
  def identifyDomain(self, text):
    examples = "Hola|SALUDAR\nHola, soy Diego|SALUDAR\nhola|SALUDAR\n¡Hola!|SALUDAR\n"
    output = self.classify(examples, text + "|")
    return output