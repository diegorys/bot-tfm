from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository
from infrastructure.dynamodb.dynamodb_dataset_repository import DynamoDBDatasetRepository
from dataset.entry import Entry

repositoryDialog = DynamoDBDialogRepository()
repositoryDataset = DynamoDBDatasetRepository()


def handle(event, context):
    dialogs = repositoryDialog.list()
    entries = []
    for dialog in dialogs:
        entry = Entry(0, dialog["text"], "", {})
        entries.append({"text": entry.text, "intent": entry.intent})
        if (not repositoryDataset.exists(entry)):
            repositoryDataset.create(entry)
    return entries
