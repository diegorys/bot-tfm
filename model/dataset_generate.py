import os
import sys
import json
import boto3


BASE_PATH = "/home/jovyan"

print("-----------")
print("DATASET GENERATE")
print("-----------")


def guardArguments() -> None:
    if 4 != len(sys.argv) and 3 != len(sys.argv):
        raise Exception("ERROR: Parameters ENVIRONMENT DATASET_VERSION_FROM? DATASET_VERSION_TO")


def getTable() -> None:
    return f"tfm-{sys.argv[1]}-dialogs"


def getVersions():
    if 3 == len(sys.argv):
        versionFrom = None
        versionTo = sys.argv[2]
    if 4 == len(sys.argv):
        versionFrom = sys.argv[2]
        versionTo = sys.argv[3]
    return versionFrom, versionTo


def getDialogs(tableName):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(tableName)
    response = table.scan()
    return response["Items"]


def getDatasetFrom(versionFrom):
    if not versionFrom:
        return []
    pathFrom = f"{BASE_PATH}/data/dataset/{versionFrom}/data.json"
    with open(pathFrom) as json_file:
        data = json.load(json_file)
    return data


def getIndexedData(data):
    indexedData = {}
    for item in data:
        indexedData[item["text"]] = item
    return indexedData


def merge(dialogs, indexedData, data):
    for dialog in dialogs:
        if dialog["text"] not in indexedData.keys():
            item = {
                "text": dialog["text"],
                "intent": "",
                "entities": {},
            }
            indexedData[item["text"]] = item
    finalData = []
    for key in indexedData.keys():
        item = indexedData[key]
        finalData.append(item)
    return finalData


def saveVersionFrom(versionFrom, versionTo, mergedData):
    dirTo = f"{BASE_PATH}/data/dataset/{versionTo}"
    pathTo = f"{dirTo}/data.json"
    print(f"Copy to {pathTo}")
    if not os.path.exists(dirTo):
        os.mkdir(dirTo)
    else:
        raise Exception(f"Error: {dirTo} already exists")
    with open(pathTo, "w", encoding="utf-8") as f:
        json.dump(mergedData, f, ensure_ascii=False, indent=4)
    print(f"Generated dataset from {versionFrom} at {pathTo}")


def main() -> None:
    try:
        guardArguments()
        versionFrom, versionTo = getVersions()
        table = getTable()
        print(f"Dataset table: {table}")
        print(f"Version from: {versionFrom}")
        print(f"Version to: {versionTo}")
        data = getDatasetFrom(versionFrom)
        print(f"Dataset {versionFrom}: {len(data)} entries")
        indexedData = getIndexedData(data)
        print(f"Getting dialogs from {table}, please wait...")
        dialogs = getDialogs(table)
        print(f"Found {len(dialogs)} dialogs.")
        mergedData = merge(dialogs, indexedData, data)
        print(f"Dataset {versionTo}: {len(mergedData)} entries")
        saveVersionFrom(versionFrom, versionTo, mergedData)
    except Exception as err:
        print(err)


main()
