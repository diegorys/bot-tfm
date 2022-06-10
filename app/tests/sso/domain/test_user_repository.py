from src.sso.domain.user_repository import UserRepository
from tests.sso.mothers.user_mother import UserMother


def test_user_repository_getByMetadata():
    repository = UserRepository()
    caregiver = UserMother.getValid("Cuidador")
    caregiver.id = 1
    dependent = UserMother.getValid("Dependiente")
    dependent.id = 2
    dependent.setKey("caregiver", caregiver.id)
    userDict = {caregiver.id: caregiver, dependent.id: dependent}
    print(f"Somos {caregiver.id} {caregiver.username}, {dependent.id}: {dependent.username}")
    print(userDict)
    repository.addRelations(userDict, caregiver)
    repository.addRelations(userDict, dependent)
    assert dependent.getCaregiver().id == caregiver.id
    ids = [user.id for user in caregiver.getDependents()]
    # assert dependent.id in ids
