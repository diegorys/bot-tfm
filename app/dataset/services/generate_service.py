from dataset.domain.entry import Entry
from dataset.domain.dataset_repository import DatasetRepository
from dialogs.domain.dialog_repository import DialogRepository


class GenerateService:
    def __init__(self, repositoryDialog: DialogRepository, repositoryDataset: DatasetRepository):
        self.repositoryDialog: DialogRepository = repositoryDialog
        self.repositoryDataset: DatasetRepository = repositoryDataset

    def execute(self):
        dialogs = self.repositoryDialog.list()
        entries = []
        for dialog in dialogs:
            text = dialog["text"]
            print(f"Processing {text}")
            entry = self.repositoryDataset.getByText(text)
            if not entry:
                print("Creating...")
                entry = Entry(0, text, "", {})
                entry = self.repositoryDataset.create(entry)
            else:
                print("Updating...")
                self.repositoryDataset.update(entry)
            entries.append({"id": entry.id, "text": entry.text, "intent": entry.intent})
        return entries
