from typing import List

from geneticAlgorithm import GeneticAlgorithm
from geneticAlgorithm.fun.Function import Function
from geneticAlgorithm.lib.models.Individual import Individual


class Selection:
    def __init__(self):
        self.state: GeneticAlgorithm = None
        self.function: Function = None
        self.population: List[Individual] = None

    def update_state(self, state: GeneticAlgorithm):
        self.state = state
        self.function = self.state.function
        self.population = self.state.population

    def selection(self, function: Function) -> List[Individual]:
        pass
