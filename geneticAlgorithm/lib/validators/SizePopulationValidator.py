class SizePopulationValidator:

    @classmethod
    def validation(cls, size_of_population):
        assert size_of_population > 0, "Size of population have to negative or zero number"
        assert size_of_population % 2 == 0, "Size of population is not even number"
