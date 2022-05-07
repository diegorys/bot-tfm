import os
import sys
if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["DIALOGS_TABLE"] = f"tfm-{environment}-dialogs"
    os.environ["DATASET_TABLE"] = f"tfm-{environment}-dataset"
import json
from infrastructure.dynamodb.dynamodb_dataset_repository import DynamoDBDatasetRepository
from dataset.services.update_service import UpdateService

repositoryDataset = DynamoDBDatasetRepository()
updateService = UpdateService(repositoryDataset)

with open("/data/dataset/trunk/data.json") as json_file:
    data = json.load(json_file)
    print(data)
print("-----------")
print("UPDATE DATASET")
output = updateService.execute(data)
print(output)
