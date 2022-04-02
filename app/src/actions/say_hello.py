import openai

class SayHello:
    def __init__(self, command):
        self.command = command

    def execute(self, user, text):
        examples = "Human: START\nRobot: Hola tú, Human\nRobot: ¿qué tal estás?\nHuman: ¡Hola!\nRobot: ¿Qué tal estás, Human?"
        request = user.name + ": " + text +"\nRobot:"
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
        # return f"Hola {user.name}"
        return response["choices"][0]["text"]
