import os
import json
import openai

openai.api_key = (
    "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"  # os.getenv("OPENAI_API_KEY")
)


def handle(event, context):
    request = event["request"]
    print(f"User input: {request}")
    openAIResponse = openai.Completion.create(
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

    bot = openAIResponse["choices"][0]["text"].replace("\n", "")
    print(f"Bot output: {bot}")

    response = {"statusCode": 200, "bot": bot}

    return response