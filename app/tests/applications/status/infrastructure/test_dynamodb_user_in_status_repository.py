from src.applications.status.infrastructure.dynamodb_user_in_status_repository import (
    DynamoDBUserInStatusRepository,
)
from tests.applications.status.mother.user_in_status_mother import UserInStatusMother


def test_save_getStatusOfgetStatusOf():
    repository = DynamoDBUserInStatusRepository()
    userInStatus = UserInStatusMother.forStatusNow("good")
    repository.save(userInStatus)
    userInStatus = UserInStatusMother.forStatusNow("bad")
    repository.save(userInStatus)
    userInStatus = UserInStatusMother.forStatusNow("sad")
    repository.save(userInStatus)
    userInStatus = UserInStatusMother.forStatusNow("happy")
    repository.save(userInStatus)

    received = repository.getStatusOf(userInStatus.user)

    assert "happy" == received.status.name
