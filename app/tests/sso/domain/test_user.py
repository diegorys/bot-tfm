from tests.sso.mothers.user_mother import UserMother

def test_user_add_dependent():
    caregiver = UserMother.forId("a")
    dependent = UserMother.forId("b")
    caregiver.addDependent(dependent)
    expected = 1

    received = len(caregiver.getDependents())

    assert received == expected