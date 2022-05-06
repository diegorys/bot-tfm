import os
import sys
import json
from dataset.services.generate_service import GenerateService
from infrastructure.dynamodb.dynamodb_dataset_repository import DynamoDBDatasetRepository
from infrastructure.dynamodb.dynamodb_dialog_repository import DynamoDBDialogRepository

if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["DIALOGS_TABLE"] = f"tfm-{environment}-dialogs"
    os.environ["DATASET_TABLE"] = f"tfm-{environment}-dataset"

repositoryDialog = DynamoDBDialogRepository()
repositoryDataset = DynamoDBDatasetRepository()
generateService = GenerateService(repositoryDialog, repositoryDataset)

print("-------------")
print(os.environ["DIALOGS_TABLE"])
print(os.environ["DATASET_TABLE"])
print("-------------")

print("GENERATE DATASET")
output = generateService.execute()
print(output)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("Saved at data.json")
