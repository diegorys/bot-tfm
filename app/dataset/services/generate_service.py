import time
from dataset.domain.entry import Entry
from dataset.domain.dataset_repository import DatasetRepository
from dialogs.domain.dialog_repository import DialogRepository


class GenerateService:
    def __init__(self, repositoryDialog: DialogRepository, repositoryDataset: DatasetRepository):
        self.repositoryDialog: DialogRepository = repositoryDialog
        self.repositoryDataset: DatasetRepository = repositoryDataset
        # with open("/data/dataset/trunk/data.json") as json_file:
        #     data = json.load(json_file)
        #     self.texts = [item["text"] for item in data]

    def execute(self):
        dialogs = self.repositoryDialog.list()
        dataEntries = self.repositoryDataset.list()
        indexedEntries = {}
        for item in dialogs:
            indexedEntries[item["text"]] = Entry(
                item["id"], item["text"], item["intent"], item["entities"]
            )
        entries = []
        for dialog in dialogs:
            time.sleep(0.03)
            text = dialog["text"]
            if "/start" != text:
                print(f"Processing {text}")
                entry = indexedEntries[text]
                if not entry:
                    print("Creating...")
                    entry = Entry(0, text, "", {})
                    entry = self.repositoryDataset.create(entry)
                # else:
                #     print("Updating...")
                #     self.repositoryDataset.update(entry)
                entries.append(
                    {
                        "id": entry.id,
                        "text": entry.text,
                        "intent": entry.intent,
                        "entities": entry.entities,
                    }
                )
        return entries
