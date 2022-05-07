import uuid


class UserSaysTemplate:
    def generate(self, text: str, entities):
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
