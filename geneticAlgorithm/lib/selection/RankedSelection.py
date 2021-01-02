from typing import List

from geneticAlgorithm import GeneticAlgorithm
from geneticAlgorithm.fun.Function import Function
from geneticAlgorithm.lib.models.Individual import Individual
from geneticAlgorithm.lib.selection.Selection import Selection


class RankedSelection(Selection):

    def __init__(self, number_of_individuals_to_swap):
        super().__init__()
        self.__number_of_individuals_to_swap = number_of_individuals_to_swap
        self.__parents_population = list()

    def selection(self, function: Function) -> List[Individual]:
        population_sorted_by_adaptation = sorted(self.population, key=lambda individual: individual.value_of_adaptation)
        list_weak_individuals = self.__extract_weak_individuals(population_sorted_by_adaptation)
        list_best_individuals = self.__extract_best_individuals(population_sorted_by_adaptation)
        self.__parents_population = self.population.copy()
        self.__parents_population = self.__list_diff(self.__parents_population, list_weak_individuals)
        self.__parents_population = self.__parents_population + list_best_individuals
        return self.__parents_population

    def update_state(self, state: GeneticAlgorithm):
        super().update_state(state)
        self.__parents_population = list()

    def __extract_weak_individuals(self, population_sorted_by_adaptation: List[Individual]) -> List[Individual]:
        selected_n_weak_individuals = []
        for item in population_sorted_by_adaptation:
            if len(selected_n_weak_individuals) == self.__number_of_individuals_to_swap:
                break
            selected_n_weak_individuals.append(item)
        return selected_n_weak_individuals

    def __extract_best_individuals(self, population_sorted_by_adaptation: List[Individual]) -> List[Individual]:
        selected_n_best_individuals = []
        population_sorted_by_adaptation.reverse()
        for item in population_sorted_by_adaptation:
            if len(selected_n_best_individuals) == self.__number_of_individuals_to_swap:
                break
            selected_n_best_individuals.append(item)
        return selected_n_best_individuals

    def __list_diff(self, list1, list2):
        out = []
        for ele in list1:
            if not ele in list2:
                out.append(ele)
        return out
