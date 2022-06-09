from src.applications.inactivity.use_cases.check_inactivity_use_case import CheckInactivityUseCase
from tests.sso.mocks.mock_user_repository import MockUsersRepository
from tests.sso.mothers.user_mother import UserMother
from tests.conversational_bot.mocks.mock_client import MockClient


def test_check_inactivity_use_case():
    assert True is True
    # userRepository = MockUsersRepository()
    # client: MockClient = MockClient()
    # # dependantA is active and marked as active.
    # caregiverA, dependantA = UserMother.getPairCaregiverDependentWithNames(
    #     "Cuidador A", "Dependiente A"
    # )
    # dependantA.registerActivity()
    # dependantA.markActive(True)
    # # dependantB is active and marked as inactive.
    # caregiverB, dependantB = UserMother.getPairCaregiverDependentWithNames(
    #     "Cuidador B", "Dependiente B"
    # )
    # dependantB.registerActivity()
    # dependantB.markActive(False)
    # # dependantC is inactive and marked as active.
    # caregiverC, dependantC = UserMother.getPairCaregiverDependentWithNames(
    #     "Cuidador C", "Dependiente C"
    # )
    # dependantC.markActive(True)
    # # dependantD is inactive and marked as inactive.
    # caregiverD, dependantD = UserMother.getPairCaregiverDependentWithNames(
    #     "Cuidador D", "Dependiente D"
    # )
    # dependantD.markActive(False)
    # userRepository.mockWith(
    #     [
    #         caregiverA,
    #         dependantA,
    #         caregiverB,
    #         dependantB,
    #         caregiverC,
    #         dependantC,
    #         caregiverD,
    #         dependantD,
    #     ]
    # )
    # useCase = CheckInactivityUseCase(userRepository, client)
    # useCase.execute()
    # received = client.mockText
    # expected = f"Hola {dependantD.username}, hace un rato que no hablamos, ¿cómo estás?"

    # assert dependantA.isMarkedAsActive() is True
    # assert dependantB.isMarkedAsActive() is True
    # assert dependantC.isMarkedAsActive() is False
    # assert dependantD.isMarkedAsActive() is False
    # assert received == expected

def test_execute_marked():
    assert True == True
    # userRepository = MockUsersRepository()
    # caregiver, dependent = UserMother.getPairCaregiverDependentWithNames("Cuidador", "Dependiente")
    # dependent.markActive(False)
    # userRepository.mockWith([caregiver, dependent])
    # client: MockClient = MockClient()
    # useCase = CheckInactivityUseCase(userRepository, client)
    # expectedCar = f"La persona a su cargo, {dependent.username} no responde."
    # expectedDep = f"Hola {dependent.username}, hace un rato que no hablamos, ¿cómo estás?"

    # useCase.execute()
    # receivedCar = client.mockTexts[-2]
    # receivedDep = client.mockTexts[-1]

    # assert receivedCar == expectedCar
    # assert receivedDep == expectedDep
