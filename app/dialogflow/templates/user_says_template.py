import uuid


class UserSaysTemplate:
    def generate(self, text: str, entities):
        keys = entities.keys()
        outputs = {}
        escapedText = text
        pieces = []
        for key in keys:
            outputs[key] = {
                "meta": f"@{key}",
                "alias": key,
            }
            escapedText = escapedText.replace(entities[key], "#")
            pieces.append({"entity": key, "value": entities[key]})
        print(outputs)
        print(pieces)
        print(escapedText)
        tokens = escapedText.split("#")
        print(tokens)
        return {
            "data": [
                {
                    "text": text,
                    "userDefined": False,
                }
            ],
            "isTemplate": False,
            "count": 0,
            "lang": "es",
            "updated": 0,
        }
