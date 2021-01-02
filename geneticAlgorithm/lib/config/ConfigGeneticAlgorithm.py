from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton
from geneticAlgorithm.lib.validators.NumberOfBitsValidator import NumberOfBitsValidator
from geneticAlgorithm.lib.validators.ProbabilityValidator import ProbabilityValidator
from geneticAlgorithm.lib.validators.SizePopulationValidator import SizePopulationValidator


class ConfigGeneticAlgorithm:
    def __init__(self, size_of_population: int,
                 probability_of_crossing: float,
                 number_points_to_crossing: int,
                 probability_of_mutation: float,
                 number_points_to_mutation: int):
        SizePopulationValidator.validation(size_of_population)
        ProbabilityValidator.validation(probability_of_crossing, 'probability_of_crossing')
        ProbabilityValidator.validation(probability_of_mutation, 'probability_of_mutation')
        NumberOfBitsValidator.validation(number_points_to_crossing, 'Crossing',
                                         GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype)
        NumberOfBitsValidator.validation(number_points_to_mutation, 'Mutation',
                                         GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype)
        self.__size_of_population = size_of_population
        self.__probability_of_crossing = probability_of_crossing
        self.number_points_to_crossing = number_points_to_crossing
        self.probability_of_mutation = probability_of_mutation
        self.number_points_to_mutation = number_points_to_mutation

    @property
    def size_of_population(self) -> int:
        return self.__size_of_population

    @size_of_population.setter
    def size_of_population(self, value: int):
        self.__size_of_population = value

    @property
    def probability_of_crossing(self) -> float:
        return self.__probability_of_crossing

    @probability_of_crossing.setter
    def probability_of_crossing(self, value: float):
        self.__probability_of_crossing = value

    @property
    def number_points_to_crossing(self) -> int:
        return self.__number_points_to_crossing

    @number_points_to_crossing.setter
    def number_points_to_crossing(self, value: int):
        self.__number_points_to_crossing = value

    @property
    def probability_of_mutation(self) -> float:
        return self.__probability_of_mutation

    @probability_of_mutation.setter
    def probability_of_mutation(self, value: float):
        self.__probability_of_mutation = value

    @property
    def number_points_to_mutation(self) -> int:
        return self.__number_points_to_mutation

    @number_points_to_mutation.setter
    def number_points_to_mutation(self, value: int):
        self.__number_points_to_mutation = value
