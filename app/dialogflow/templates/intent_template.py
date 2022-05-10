import uuid
from expert_system.domain import intents


class IntentTemplate:
    def generate(self, intent: str):
        parameters = []
        speech = []
        responsePhrase = ""
        if intent in intents.keys():
            slots = intents[intent]
            for slot in slots:
                name = slot["name"]
                dataType = slot["name"]
                value = slot["name"]
                if "cuando" == slot["name"]:
                    name = "date-time"
                    dataType = "sys.date-time"
                    value = "date-time"
                if "" == responsePhrase:
                    responsePhrase = "Recibido"
                responsePhrase += f" {name}: ${name}"
                parameters.append(
                    {
                        "id": "37ffd186-5803-44b9-ad7c-994e13f362bf",
                        "name": f"{name}",
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
        if "" == responsePhrase:
            responsePhrase = f"Recibido {intent.lower()}"
        speech.append(responsePhrase)
        return {
            "id": str(uuid.uuid4()),
            "name": intent,
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
