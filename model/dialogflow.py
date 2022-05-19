import json
import sys
from dialogflow.generate_service import GenerateService

BASE_PATH="/home/jovyan"

print("-----------")
print("DIALOGFLOW GENERATE")
print("-----------")



def getVersions():
    if 3 != len(sys.argv):
        raise Exception("ERROR: Required DATASET_VERSION and MODEL_VERSION")
    dataVersion = sys.argv[1]
    modelVersion = sys.argv[2]
    return dataVersion, modelVersion

def getData(dataVersion):
    with open(f"{BASE_PATH}/data/dataset/{dataVersion}/data_train.json") as json_file:
        data = json.load(json_file)
    return data

try:
    dataVersion, modelVersion = getVersions()
    data = getData(dataVersion)
    print(f"Dataset version: {dataVersion}, Model version: {modelVersion}")
    generateService = GenerateService(BASE_PATH)
    generateService.execute(data, dataVersion, modelVersion)
except Exception as err:
    print(err)

