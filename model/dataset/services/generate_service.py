import os
import boto3
from dataset.domain.entry import Entry
from dataset.domain.dataset_repository import DatasetRepository


class GenerateService:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def execute(self):
        dialogs = self.listDialogs()
        indexedEntries = {}
        for item in dataEntries:
            indexedEntries[item["text"]] = Entry(
                item["id"], item["text"], item["intent"], item["entities"]
            )
        entries = []
        for dialog in dialogs:
            # time.sleep(0.03)
            text = dialog["text"]
            if "/start" != text:
                print(f"Processing {text}")
                if text not in indexedEntries:
                    print("Creating...")
                    entry = Entry(0, text, "", {})
                    entry = self.repositoryDataset.create(entry)
                else:
                    entry = indexedEntries[text]
                entries.append(
                    {
                        "id": entry.id,
                        "text": entry.text,
                        "intent": entry.intent,
                        "entities": entry.entities,
                    }
                )
        return entries

    def listDialogs(self):
        table = self.dynamodb.Table(os.environ["DIALOGS_TABLE"])
        response = table.scan()
        return response["Items"]

    def listDataset(self):
        table = self.dynamodb.Table(os.environ["DATASET_TABLE"])
        response = table.scan()
        return response["Items"]
