import json
import os
import sys

TELEGRAM_TOKEN = {
    "test": "***REMOVED***",
    "prod": "***REMOVED***",
}
if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["USERS_TABLE"] = f"tfm-{environment}-users"
    os.environ["TELEGRAM_TOKEN"] = TELEGRAM_TOKEN[environment]

from notifications.infrastructure.aws_telegram_notifications import TELEGRAM_TOKEN, handle as send

message = sys.argv[2]
print("-------------")
print(os.environ["USERS_TABLE"])
print("-------------")

print("SEND NOTIFICATION")
send({"message": message}, None)

# import boto3
# client = boto3.client('lambda')

# response = client.invoke(
#     FunctionName=f"tfm-{environment}-notify",
#     # InvocationType='Event',
#     Payload=json.dumps({"message": message})
# )
# print(json.loads(response['Payload'].read()))
# print("\n")
