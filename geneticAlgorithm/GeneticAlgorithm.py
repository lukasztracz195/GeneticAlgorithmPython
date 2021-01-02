import random
from typing import *

from geneticAlgorithm.fun.Function import Function
from geneticAlgorithm.lib.config.ConfigGeneticAlgorithm import ConfigGeneticAlgorithm
from geneticAlgorithm.lib.models.Individual import Individual
from geneticAlgorithm.lib.models.Pair import Pair
from geneticAlgorithm.lib.selection.Selection import Selection
from geneticAlgorithm.lib.stopconditionals.StopConditional import StopConditional


class GeneticAlgorithm:
    def __init__(self, config: ConfigGeneticAlgorithm,
                 stop_condition: StopConditional,
                 function: Function,
                 selection_algorithm: Selection,
                 debug: bool):
        self.__config = config
        self.__stop_condition = stop_condition
        self.__function = function
        self.__selection_algorithm = selection_algorithm
        self.__debug = debug

        self.__number_individuals_for_rank_selection: int = 0
        self.__population: List[Individual] = []
        self.__parents_population: List[Individual] = []
        self.__selected_parents_population: Set[int] = set()
        self.__number_of_cycle = 0
        self.__stop_condition.update_state(self)
        self.__history_max_value_adaption: List[float] = list()

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        self.__config = value

    @property
    def stop_conditional(self):
        return self.__stop_conditional

    @stop_conditional.setter
    def stop_conditional(self, value):
        self.__stop_conditional = value

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        self.__function = value

    @property
    def number_individuals_for_rank_selection(self):
        return self.__number_individuals_for_rank_selection

    @number_individuals_for_rank_selection.setter
    def number_individuals_for_rank_selection(self, value):
        self.__number_individuals_for_rank_selection = value

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def parents_population(self):
        return self.__parents_population

    @parents_population.setter
    def parents_population(self, value):
        self.__parents_population = value

    @property
    def number_of_cycle(self):
        return self.__number_of_cycle

    @number_of_cycle.setter
    def number_of_cycle(self, value):
        self.__number_of_cycle = value

    @property
    def history_max_value_adaption(self) -> List[float]:
        return self.__history_max_value_adaption

    @history_max_value_adaption.setter
    def history_max_value_adaption(self, value):
        self.__history_max_value_adaption = value

    def start(self):
        self.__generate_population()
        self.__number_of_cycle = 0

        while True:
            self.__selection()
            self.__crossing()
            self.__mutation()
            self.__number_of_cycle += 1
            self.__stop_condition.update_state(self)
            if self.__debug:
                for item in self.population:
                    print(item)
                print("Obieg ", self.__number_of_cycle, " rozmiar populacji: ", len(self.population))
            self.__history_max_value_adaption.append(self.__find_max_value_adaption_in_population())
            if self.__stop_condition.can_stop():
                break

    def __generate_population(self) -> List[Individual]:
        population = set()
        while len(population) < self.__config.size_of_population:
            new_individual = Individual.generate()
            if new_individual in population:
                pass
            else:

                population.add(new_individual)
        self.__population = list(population)
        return self.__population

    def __crossing(self):
        self.__population.clear()
        self.__selected_parents_population.clear()
        self.__selected_parents_population = self.__parents_population.copy()
        while True:
            pair = self.__select_pair_of_parents()
            pair.crossing(self.__config.probability_of_crossing, self.__config.number_points_to_crossing)
            self.__population.append(pair.one)
            self.__population.append(pair.two)
            if len(self.population) == self.__config.size_of_population:
                break
        self.__set_adaptation_value_for_population()

    def __select_pair_of_parents(self) -> Pair:
        selected_of_indexes = []
        while True:
            set_of_indexes = set(range(len(self.__selected_parents_population)))
            index = random.randint(0, len(set_of_indexes) - 1)
            if index in selected_of_indexes:
                pass
            else:
                selected_of_indexes.append(index)
            if len(selected_of_indexes) == 2:
                break
        parent1 = list(self.__selected_parents_population)[selected_of_indexes[0]]
        parent2 = list(self.__selected_parents_population)[selected_of_indexes[1]]
        return Pair(parent1, parent2)

    def __mutation(self):

        probability_of_mutation = self.__config.probability_of_mutation
        for individual in self.population:
            individual.mutation(probability_of_mutation=probability_of_mutation,
                                number_bits_for_mutation=self.__config.number_points_to_mutation)
        self.__set_adaptation_value_for_population()

    def __selection(self):
        self.__selection_algorithm.update_state(self)
        self.__parents_population.clear()
        self.__set_adaptation_value_for_population()
        self.__parents_population = self.__selection_algorithm.selection(self.__function)

    def __set_adaptation_value_for_population(self):
        for item in self.__population:
            dictionary = {'x': item.phenotype_x,
                          'y': item.phenotype_y}
            self.__function.update_parameters(dictionary)
            value_of_adaption = self.__function.count_value_function()
            item.value_of_adaptation = value_of_adaption

    def __find_max_value_adaption_in_population(self):
        max = 0.0
        for item in self.__population:
            if item.value_of_adaptation > max:
                max = item.value_of_adaptation
        return max

# ind = Individual(5, 5)
# # phenotype ( -7.999 ) -> genotype
# # |SIGN|INTEGER_PART  |                   FLOATING_OF_PART                       |
# # [ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ]
# #   0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15 | indexes
# #   0    2    1    0   -1   -2   -3   -4   -5   -6    -7   -8   -9  -10  -11  -12 | exponents power of 2
# genotype = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# fenotype = ind.generate_phenotype_from_genotype(genotype)
# print("genotype: ", genotype)
# print("fenotype: ", fenotype)
