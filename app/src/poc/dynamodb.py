import boto3
from boto3.dynamodb.conditions import Attr
from botocore.config import Config

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("tfm-test-dialogs")

date = '2022-04-20 18:38:20+00:00'
text = 'afsefaef'

response = table.scan(
    FilterExpression=Attr("date").eq(date) & Attr("text").eq(text)
)

print(response['Items'])

res = len(response['Items']) > 0
print(res)
