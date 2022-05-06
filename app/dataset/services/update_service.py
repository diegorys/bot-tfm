from dataset.domain.entry import Entry
from dataset.domain.dataset_repository import DatasetRepository


class UpdateService:
    def __init__(self, repositoryDataset: DatasetRepository):
        self.repositoryDataset: DatasetRepository = repositoryDataset

    def execute(self, lines):
        for line in lines:
            entry = Entry(line["id"], line["text"], line["intent"], {})
            print(f"Updating {line['text']}: {line['intent']}")
            response = self.repositoryDataset.update(entry)
            print(response)
