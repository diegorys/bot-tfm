class RegisterMedicineUseCase:
    # def __init__(self, repository):
    #     self.repository = repository

    def execute(self, medicine):
        print(f"SAVE MEDICINE {medicine.name}")
        # self.repository.save(medicine)
