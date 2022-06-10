from src.sso.domain.user import User
from src.sso.infrastructure.dynamodb_user_respository import DynamoDBUsersRepository
from tests.sso.mothers.user_mother import UserMother


def test_save_list():
    userRepository = DynamoDBUsersRepository()
    caregiver, dependent = UserMother.getPairCaregiverDependentWithNames(
        "Cuidador A", "Dependiente A"
    )
    caregiver.setKey("a_key", "a_value")
    dependent.setKey("b_key", "b_value")
    receivedCaregiver = None
    receivedDependent = None

    userRepository.save(caregiver)
    userRepository.save(dependent)
    users = userRepository.list()
    for user in users:
        print(f"{user.id}: {user.username}")
        realUser: User = user
        if realUser.username == "Cuidador A":
            receivedCaregiver = realUser
        elif realUser.username == "Dependiente A":
            receivedDependent = realUser

    assert receivedCaregiver is not None
    assert receivedDependent is not None
    assert "a_value" == receivedCaregiver.getKey("a_key")
    assert "b_value" == receivedDependent.getKey("b_key")

    receivedCaregiver.addDependent(receivedDependent)
    receivedDependent.setCaregiver(receivedCaregiver)

    updatedCaregiver = None
    updatedDependent = None

    userRepository.save(receivedCaregiver)
    userRepository.save(receivedDependent)
    users = userRepository.list()
    for user in users:
        realUser: User = user
        print(f"{realUser.id}, {realUser.metadata}")
        if updatedCaregiver is None and realUser.username == "Cuidador A":
            updatedCaregiver = realUser
        elif updatedDependent is None and realUser.username == "Dependiente A":
            updatedDependent = realUser
    print(f"-----------DEPENDENTS {updatedCaregiver.id}")
    print(updatedCaregiver.metadata["dependents"])
    assert updatedCaregiver is not None
    # assert len(updatedCaregiver.getDependents()) == 1
    assert updatedDependent is not None
