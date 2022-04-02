import openai


class RememberMedicine:
    def __init__(self, command):
        self.command = command

    def execute(self, user, text):
        examples = "Tengo que tomar un ibuprofeno los lunes|TOMAR#IBUPROFENO|LUNES.\nA las 12:00 me toca el paracetamol|TOMAR#PARACETAMOL|12:00."
        request = text
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
            stop=["\n"],
        )
        return "Vale, te recordaré que te tomes la medicina"#response["choices"][0]["text"]
