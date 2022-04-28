from infrastructure.dynamodb.dynamodb_dataset_repository import DynamoDBDatasetRepository
from dataset.entry import Entry

repositoryDataset = DynamoDBDatasetRepository()


def handle(event, context):
    for line in event:
        entry = Entry(line['id'], line['text'], line['intent'], {})
        repositoryDataset.update(entry)
