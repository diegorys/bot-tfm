import json
import sys
from dialogflow.generate_service import GenerateService

BASE_PATH = "/home/jovyan"

print("-----------")
print("DIALOGFLOW GENERATE")
print("-----------")

def guardArguments() -> None:
    if 2 != len(sys.argv):
        raise Exception("ERROR: Required DATASET_VERSION")

def getVersion():
    datasetVersion = sys.argv[1]
    return datasetVersion


def getData(datasetVersion):
    with open(f"{BASE_PATH}/data/dataset/{datasetVersion}/data_train.json") as json_file:
        data = json.load(json_file)
    return data


def main() -> None:
    try:
        guardArguments()
        datasetVersion = getVersion()
        data = getData(datasetVersion)
        languageModel = "dialogflow"
        print(f"Dataset version: {datasetVersion}")
        print(f"Language model: {languageModel}")
        generateService = GenerateService(BASE_PATH)
        generateService.execute(data, datasetVersion)
    except Exception as err:
        print(err)

main()
