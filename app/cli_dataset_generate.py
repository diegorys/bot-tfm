import os
import sys
import json

if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["DIALOGS_TABLE"] = f"tfm-{environment}-dialogs"
    os.environ["DATASET_TABLE"] = f"tfm-{environment}-dataset"

from language_model.generate import handle as generate


print("-------------")
print(os.environ["DIALOGS_TABLE"])
print(os.environ["DATASET_TABLE"])
print("-------------")

print("GENERATE DATASET")
output = generate(None, None)
print(output)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("Saved at data.json")
