# -*- coding: utf-8 -*-

from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository
from infrastructure.dynamodb.dynamodb_dataset_repository import DynamoDBDatasetRepository
from language_model.entry import Entry

repositoryDialog = DynamoDBDialogRepository()
repositoryDataset = DynamoDBDatasetRepository()


def handle(event, context):
    dialogs = repositoryDialog.list()
    entries = []
    for dialog in dialogs:
        text = dialog["text"]
        print(f"Processing {text}")
        entry = repositoryDataset.getByText(text)
        if not entry:
            print("Creating...")
            entry = Entry(0, text, "", {})
            entry = repositoryDataset.create(entry)
        else:
            print("Updating...")
            repositoryDataset.update(entry)
        entries.append({"id": entry.id, "text": entry.text, "intent": entry.intent})
    return entries
