import os
import pytest
os.environ["MEDICATION_USER_TABLE"] = "tfm-test-medication-user"
from src.applications.medical.domain.medication_user import MedicationUser
from src.applications.medical.infrastructure.dynamodb_medication_user_repository import DynamoDBMedicationUserRepository
from tests.applications.medical.mothers.medication_user_mother import MedicationUserMother

@pytest.mark.skip(reason="No está desplegada la infraestructura en test")
def test_save():
    repository = DynamoDBMedicationUserRepository()
    medicationUser = MedicationUserMother.getValid()

    repository.save(medicationUser)

    assert True == False