import openai


class DetectStatus:
    def __init__(self, command):
        self.command = command

    def execute(self, user, text):
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
