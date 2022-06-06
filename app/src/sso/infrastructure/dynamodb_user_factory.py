from src.sso.domain.user import User


class DynamoDBUserFactory:
    def create(item):
        user = User(item["name"], {"telegram_id": item["telegram_id"], "username": item["name"]})
        if "caregiver" in item.keys():
            user.metadata["caregiver"] = item["caregiver"]
        if "dependents" in item.keys():
            user.metadata["dependents"] = []
            for dependent in item["dependents"]:
                user.metadata["dependents"].append(int(dependent))
        return user
