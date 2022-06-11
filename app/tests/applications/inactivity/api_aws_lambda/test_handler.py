import os

os.environ["STAGE"] = "test"
from src.applications.inactivity.api_aws_lambda.handler import handle


def test_handle():
    result = handle(None, None)
    assert 200 == result["statusCode"]
