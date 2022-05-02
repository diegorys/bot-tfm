import os
import sys

if 1 < len(sys.argv):
    environment = sys.argv[1]
    os.environ["USERS_TABLE"] = f"tfm-{environment}-users"

from notifications.infrastructure.aws_telegram_notifications import handle as send

message = sys.argv[2]
print("-------------")
print(os.environ["USERS_TABLE"])
print("-------------")

print("SEND NOTIFICATION")
send({"message": message}, None)
