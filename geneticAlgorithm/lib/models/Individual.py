import random
from typing import *

from geneticAlgorithm.lib.bitstools.BitInverter import BitInverter
from geneticAlgorithm.lib.bitstools.BitsRandomizer import BitsRandomizer
from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton
from geneticAlgorithm.lib.decider.ProbabilityDeceider import ProbabilityDecider
from geneticAlgorithm.lib.converters.Coder import Coder
from geneticAlgorithm.lib.converters.Decoder import Decoder


class Individual:
    def __init__(self, x: float, y: float):
        self.__phenotype_x: float = x
        self.__phenotype_y: float = y
        self.__genotype_x: List[int] = Coder.code(x)
        self.__genotype_y: List[int] = Coder.code(y)
        self.__value_of_adaptation: float = 0
        self.__probability_of_selection: float = 0

    @classmethod
    def init(cls, individual):
        individual = Individual(individual.phenotype_x,
                                individual.phenotype_y)

        individual.__genotype_x = individual.genotype_x
        individual.__genotype_y = individual.genotype_y
        individual.__value_of_adaptation = individual.value_of_adaptation
        individual.__probability_of_selection = individual.probability_of_selection
        return individual

    def __copy__(self):
        new_individual = Individual(self.__phenotype_x, self.__phenotype_y)
        new_individual.value_of_adaptation = self.value_of_adaptation
        new_individual.probability_of_selection = self.probability_of_selection
        return new_individual

    @classmethod
    def generate(cls):
        start = GenotypePhenotypeConfigSingleton().min_phenotype_value
        stop = GenotypePhenotypeConfigSingleton().max_phenotype_value
        phenotype_x = random.uniform(start, stop)
        phenotype_y = random.uniform(start, stop)
        return Individual(phenotype_x, phenotype_y)

    def __hash__(self):
        return hash((tuple(self.__genotype_x), tuple(self.__genotype_y), self.__phenotype_y, self.__phenotype_x, self.__value_of_adaptation))

    def __eq__(self, other):
        return self.__genotype_x == other.genotype_x and self.__genotype_y == other.genotype_y

    def __lt__(self, other):
        return self.value_of_adaptation < other.get_value_of_adaptation()

    def __repr__(self):
        return repr(self.value_of_adaptation)

    def __str__(self):
        return '{\nphenotype_x: %s\tphenotype_y: %s\ngenotype_x: %s\tgenotype_y: %s\nvalue_of_adaptation: %s\n}' % (
            self.__phenotype_x, self.__phenotype_y, self.__genotype_x, self.__genotype_y, self.value_of_adaptation)

    @property
    def value_of_adaptation(self) -> float:
        return self.__value_of_adaptation

    @value_of_adaptation.setter
    def value_of_adaptation(self, value: float):
        self.__value_of_adaptation = value

    @property
    def probability_of_selection(self) -> float:
        return self.__probability_of_selection

    @probability_of_selection.setter
    def probability_of_selection(self, value: float):
        self.__probability_of_selection = value

    @property
    def genotype_x(self) -> List[int]:
        return self.__genotype_x

    @genotype_x.setter
    def genotype_x(self, value: List[int]):
        self.__phenotype_x = Decoder.decode(value)
        self.__genotype_x = value

    @property
    def genotype_y(self) -> List[int]:
        return self.__genotype_y

    @genotype_y.setter
    def genotype_y(self, value: List[int]):
        self.__phenotype_y = Decoder.decode(value)
        self.__genotype_y = value

    @property
    def phenotype_x(self) -> float:
        return self.__phenotype_x

    @phenotype_x.setter
    def phenotype_x(self, value: float):
        self.__genotype_x = Coder.code(value)
        self.__phenotype_x = value

    @property
    def phenotype_y(self) -> float:
        return self.__phenotype_y

    @phenotype_y.setter
    def phenotype_y(self, value: float):
        self.__genotype_y = Coder.code(value)
        self.__phenotype_y = value

    def mutation(self, probability_of_mutation, number_bits_for_mutation):
        mutation_is_accepted = ProbabilityDecider.decide_with_probability(probability_of_mutation)
        if mutation_is_accepted:
            dict_x = Individual.mutation_of_genotype(self.__genotype_x, number_bits_for_mutation)
            self.__genotype_x = dict_x['genotype']
            self.__phenotype_x = dict_x['phenotype']

            dict_y = Individual.mutation_of_genotype(self.__genotype_y, number_bits_for_mutation)
            self.__genotype_y = dict_y['genotype']
            self.__phenotype_y = dict_y['phenotype']

    @classmethod
    def mutation_of_genotype(cls, genotype, number_bits_for_mutation):
        new_genotype = list(genotype)
        indexes_of_bits_for_mutation_for_genotype_x = BitsRandomizer.random_without_returning(
            GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype, number_bits_for_mutation)
        for index_to_invert in indexes_of_bits_for_mutation_for_genotype_x:
            genotype[index_to_invert] = BitInverter.invert(genotype[index_to_invert])
        new_phenotype = Decoder.decode(new_genotype)
        return {'genotype': new_genotype,
                'phenotype': new_phenotype}
