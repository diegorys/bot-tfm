import uuid


class UserSaysTemplate:
    def generate(self, text: str, entities):
        keys = entities.keys()
        escapedText = text
        pieces = []
        for key in keys:
            escapedText = escapedText.replace(entities[key], "#")
            pieces.append(
                {"text": entities[key], "meta": f"@{key}", "alias": key, "userDefined": False}
            )
        tokens = escapedText.split("#")
        data = []
        i = 0
        for token in tokens:
            if "" != token:
                dataItem = {
                    "text": token,
                    "userDefined": False,
                }
                data.append(dataItem)
            if i < len(pieces):
                data.append(pieces[i])
                i += 1
        return {
            "data": data,
            "isTemplate": False,
            "count": 0,
            "lang": "es",
            "updated": 0,
        }
