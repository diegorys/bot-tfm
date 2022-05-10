from dataset.domain.entry import Entry
from dataset.domain.dataset_repository import DatasetRepository
from dataset.intents import intents


class UpdateService:
    def __init__(self, repositoryDataset: DatasetRepository):
        self.repositoryDataset: DatasetRepository = repositoryDataset

    def execute(self, lines):
        unknownIntents = []
        notClassified = 0
        for line in lines:
            print(line["text"])
            intent = line["intent"]
            if intent in intents:
                entry = Entry(line["id"], line["text"], line["intent"], line["entities"])
                print(f"Updating {line['text']}: {intent}")
                response = self.repositoryDataset.update(entry)
                print(response)
                print("Done!")
            else:
                if "" != intent:
                    unknownIntents.append(intent)
                    print(f"WARNING! UNKNOWN INTENT: {intent}")
                else:
                    notClassified += 1
        print(unknownIntents)
        print(f"Not classified intents: {notClassified}")
