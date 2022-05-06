from dataset.domain.entry import Entry


class DatasetRepository:
    def create(self, entry: Entry):
        pass

    def update(self, entry: Entry):
        pass

    def list(self):
        pass

    def truncate(self):
        pass

    def exists(self, entry):
        pass

    def getByText(self, text):
        pass
