import os
import boto3
import pytest
from src.events.infrastructure.dynamodb_event_repository import DynamoDBEventRepository
from tests.events.mother.event_mother import EventMother


def test_save():
    clear()
    repository = DynamoDBEventRepository()
    event = EventMother.getValid()
    event.user.metadata["telegram_id"] = "1234"

    try:
        repository.save(event)
    except Exception as e:
        raise pytest.fail("{0}".format(e))


def test_list_empty():
    clear()
    repository = DynamoDBEventRepository()

    events = repository.list()

    assert 0 == len(events)


def test_list_five():
    clear()
    repository = DynamoDBEventRepository()
    for i in range(0, 5):
        event = EventMother.getValid()
        event.user.metadata["telegram_id"] = f"{i}"
        repository.save(event)

    try:
        repository.list()
    except Exception as e:
        raise pytest.fail("{0}".format(e))


def clear():
    stage = os.environ["STAGE"]
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(f"tfm-{stage}-events")
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan["Items"]:
            batch.delete_item(Key={"id": each["id"]})
