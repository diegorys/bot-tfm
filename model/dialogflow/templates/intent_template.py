import uuid
from expert_system.domain import intents
from expert_system.domain import responses


class IntentTemplate:

    def generateResponse(self, template: str, entities) -> str:
        text = template
        for entity in entities.keys():
            value = entities[entity]
            text = text.replace(f"[{entity}]", value)
        return text

    def generate(self, intent: str):
        parameters = []
        speech = []
        responsePhrase = ""
        if intent in intents.keys():
            slots = intents[intent]
            entities = {}
            for slot in slots:
                name = slot["name"]
                dataType = slot["name"]
                value = slot["name"]
                if "cuando" == slot["name"]:
                    name = "date-time"
                    dataType = "sys.date-time"
                    value = "date-time"
                if intent in responses.keys():
                    entities[slot["name"]] = f"${value}"
                else:
                    if "" == responsePhrase:
                        responsePhrase = "Recibido"
                    responsePhrase += f" {name}: ${value}"
                parameters.append(
                    {
                        "id": "37ffd186-5803-44b9-ad7c-994e13f362bf",
                        "name": f"{name}",
                        "auto": True,
                        "required": True,
                        "dataType": f"@{dataType}",
                        "value": f"${value}",
                        "defaultValue": "",
                        "isList": slot["required"],
                        "prompts": [{"lang": "es", "value": f"Indica {name}"}],
                        "promptMessages": [],
                        "noMatchPromptMessages": [],
                        "noInputPromptMessages": [],
                        "outputDialogContexts": [],
                    }
                )
        if intent in responses.keys():
            for response in responses[intent]:
                if "" != response:
                    responsePhrase = self.generateResponse(response, entities)
                    speech.append(responsePhrase)
        if "" == responsePhrase:
            humanizedIntent = intent.lower().replace("_", " ")
            responsePhrase = (
                f"Entiendo que quieres {humanizedIntent}, pero aún no estoy preparado para eso."
            )
        speech.append(responsePhrase)
        return {
            "id": str(uuid.uuid4()),
            "name": intent,
            "auto": True,
            "contexts": [],
            "responses": [
                {
                    "resetContexts": False,
                    "action": "",
                    "affectedContexts": [],
                    "parameters": parameters,
                    "messages": [
                        {
                            "type": "0",
                            "title": "",
                            "textToSpeech": "",
                            "lang": "es",
                            "speech": speech,
                            "condition": "",
                        }
                    ],
                    "speech": [],
                }
            ],
            "priority": 500000,
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": [],
        }
