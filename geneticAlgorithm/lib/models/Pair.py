from typing import Dict

from geneticAlgorithm.lib.models import Individual
from geneticAlgorithm.lib.bitstools.BitsRandomizer import BitsRandomizer
from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton
from geneticAlgorithm.lib.decider.ProbabilityDeceider import ProbabilityDecider


class Pair:
    def __init__(self, one: Individual, two: Individual):
        self.__one: Individual = one
        self.__two: Individual = two

    def __copy__(self):
        return Pair(self.__one, self.__two)

    @property
    def one(self) -> Individual:
        return self.__one

    @one.setter
    def one(self, value: Individual):
        self.__one = value

    @property
    def two(self) -> Individual:
        return self.__two

    @two.setter
    def two(self, value: Individual):
        self.__two = value

    def crossing(self, probability_of_crossing: float, number_of_locus_to_crossing: int):
        crossing_is_accepted = ProbabilityDecider.decide_with_probability(probability_of_crossing)
        if crossing_is_accepted:
            self.__crossing_of_individuals(number_of_locus_to_crossing)

    def __crossing_of_individuals(self, number_of_locus_to_crossing):
        genotype_x_one = self.__one.genotype_x
        genotype_y_one = self.__one.genotype_y
        genotype_x_two = self.__two.genotype_x
        genotype_y_two = self.__two.genotype_y

        dict_genotype_x = self.__crossing_of_genotypes(genotype_x_one, genotype_x_two, number_of_locus_to_crossing)
        self.__one.genotype_x = dict_genotype_x['genotype_one']
        self.__two.genotype_x = dict_genotype_x['genotype_two']

        dict_genotype_y = self.__crossing_of_genotypes(genotype_y_one, genotype_y_two, number_of_locus_to_crossing)
        self.__one.genotype_y = dict_genotype_y['genotype_one']
        self.__two.genotype_y = dict_genotype_y['genotype_two']

    def __crossing_of_genotypes(self, genotype_one, genotype_two, number_bits_for_crossing) -> Dict:
        new_genotype_one = list(genotype_one)
        new_genotype_two = list(genotype_two)
        indexes_of_bits_for_crossing_for_genotype = BitsRandomizer.random_without_returning(
            GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype, number_bits_for_crossing)
        for index_for_crossing in indexes_of_bits_for_crossing_for_genotype:
            tmp_bit_value = new_genotype_one[index_for_crossing]
            new_genotype_one[index_for_crossing] = new_genotype_two[index_for_crossing]
            new_genotype_two[index_for_crossing] = tmp_bit_value
        return {'genotype_one': new_genotype_one,
                'genotype_two': new_genotype_two}
