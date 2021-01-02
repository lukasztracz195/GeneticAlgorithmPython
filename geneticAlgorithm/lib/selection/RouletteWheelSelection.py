import random
from typing import List

from geneticAlgorithm import GeneticAlgorithm
from geneticAlgorithm.fun.Function import Function
from geneticAlgorithm.lib.models.Individual import Individual
from geneticAlgorithm.lib.selection.Selection import Selection


class RouletteWheelSelection(Selection):

    def __init__(self):
        super().__init__()
        self.__parents_population = list()

    def selection(self, function: Function) -> List[Individual]:
        self.__init_roulette_wheel()
        self.__random_parent_population()
        return self.__parents_population

    def update_state(self, state: GeneticAlgorithm):
        super().update_state(state)
        self.__parents_population = list()

    def __init_roulette_wheel(self):
        self.__set_adaptation_value_for_population()
        sum_adaption_value = 0.0
        for individual in self.population:
            sum_adaption_value += individual.value_of_adaptation

        for individual in self.population:
            individual.probability_of_selection = individual.value_of_adaptation / sum_adaption_value
        start = 0
        for individual in self.population:
            individual.start = start
            individual.stop = start + individual.probability_of_selection
            start = individual.stop

    def __random_parent_population(self):
        self.__parents_population.clear()
        while True:
            random_probability = random.random()
            for individual in self.population:
                if individual.is_selected(random_probability):
                    parent_individual = Individual.init(individual)
                    self.__parents_population.append(parent_individual)
                    break
            if len(self.__parents_population) == self.state.config.size_of_population:
                break

    def __set_adaptation_value_for_population(self):
        for item in self.population:
            dictionary = {'x': item.phenotype_x,
                          'y': item.phenotype_y}
            self.function.update_parameters(dictionary)
            value_of_adaption = self.function.count_value_function()
            item.value_of_adaptation = value_of_adaption
