import os
import pytest

os.environ["STAGE"] = "test"
from src.applications.inactivity.api_aws_lambda.handler import handle


@pytest.mark.skip(reason="infrastructure")
def test_handle():
    result = handle(None, None)
    assert 200 == result["statusCode"]
