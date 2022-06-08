from src.sso.domain.user import User


class DynamoDBUserFactory:
    def create(item):
        baseKeys = ["id", "name", "caregiver", "dependents"]
        user = User(item["name"])
        user.id = item["id"]
        if "caregiver" in item.keys():
            user.metadata["caregiver"] = item["caregiver"]
        if "dependents" in item.keys():
            user.metadata["dependents"] = []
            for dependent in item["dependents"]:
                user.metadata["dependents"].append(dependent)
        for key in item.keys():
            if key not in baseKeys:
                user.metadata[key] = item[key]
        return user
