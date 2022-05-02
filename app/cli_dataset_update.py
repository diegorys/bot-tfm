import os
import sys
import json

if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["DIALOGS_TABLE"] = f"tfm-{environment}-dialogs"
    os.environ["DATASET_TABLE"] = f"tfm-{environment}-dataset"

from language_model.generate import handle as generate
from language_model.update import handle as update

with open('data.json') as json_file:
    data = json.load(json_file)
    print(data)
print('-----------')
print('UPDATE DATASET')
output = update(data, None)
print(output)
