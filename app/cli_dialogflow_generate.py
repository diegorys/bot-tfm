import json
import sys
from dialogflow.services.generate_service import GenerateService

if 3 == len(sys.argv):
    DATASET_VERSION = sys.argv[1]
    MODEL_VERSION = sys.argv[2]
    print(f"Dataset version: {DATASET_VERSION}, Model version: {MODEL_VERSION}")
else:
    print("ERROR: Required DATASET_VERSION and MODEL_VERSION")
    exit(1)


generateService = GenerateService()


with open(f"/data/dataset/{DATASET_VERSION}/data_train.json") as json_file:
    data = json.load(json_file)
print("-----------")
print("DIALOGFLOW GENERATE")
generateService.execute(data, DATASET_VERSION, MODEL_VERSION)
