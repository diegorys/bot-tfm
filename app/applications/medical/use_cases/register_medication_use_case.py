class RegisterMedicationUseCase:
    # def __init__(self, repository):
    #     self.repository = repository

    def execute(self, medicine, datetime):
        print(f"SAVE MEDICINE {medicine} AT {datetime}")
        # self.repository.save(medicine)
