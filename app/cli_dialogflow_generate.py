import json
from dialogflow.services.generate_service import GenerateService

generateService = GenerateService()


with open("/data/dataset/trunk/data.json") as json_file:
    data = json.load(json_file)
    print(data)
print("-----------")
print("DIALOGFLOW GENERATE")
generateService.execute(data, "/data/dialogflow/trunk")
