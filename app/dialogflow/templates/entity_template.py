import uuid


class EntityTemplate:
    def generate(self, name: str):
        return {
            "id": str(uuid.uuid4()),
            "name": name,
            "isOverridable": True,
            "isEnum": False,
            "isRegexp": False,
            "automatedExpansion": False,
            "allowFuzzyExtraction": False,
        }
