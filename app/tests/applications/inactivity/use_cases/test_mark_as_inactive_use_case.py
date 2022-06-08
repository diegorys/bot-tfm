from src.applications.inactivity.use_cases.mark_as_inactive_use_case import MarkASInactiveUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother


def test_mark_as_inactive_use_case():
    userRepository = MockUsersRepository()
    # dependantA is active and marked as active.
    caregiverA, dependantA = UserMother.getPairCaregiverDependentWithNames("Cuidador A", "Dependiente A")
    dependantA.registerActivity()
    dependantA.markActive(True)
    # dependantB is active and marked as inactive.
    caregiverB, dependantB = UserMother.getPairCaregiverDependentWithNames("Cuidador B", "Dependiente B")
    dependantB.registerActivity()
    dependantB.markActive(False)
    # dependantC is inactive and marked as active.
    caregiverC, dependantC = UserMother.getPairCaregiverDependentWithNames("Cuidador C", "Dependiente C")
    dependantC.markActive(True)
    # dependantD is inactive and marked as inactive.
    caregiverD, dependantD = UserMother.getPairCaregiverDependentWithNames("Cuidador D", "Dependiente D")
    dependantD.markActive(False)
    userRepository.mockWith(
        [
            caregiverA,
            dependantA,
            caregiverB,
            dependantB,
            caregiverC,
            dependantC,
            caregiverD,
            dependantD,
        ]
    )
    useCase = MarkASInactiveUseCase(userRepository)
    useCase.execute()
    
    assert dependantA.isMarkedAsActive() is True
    assert dependantB.isMarkedAsActive() is True
    assert dependantC.isMarkedAsActive() is False
    assert dependantD.isMarkedAsActive() is False
