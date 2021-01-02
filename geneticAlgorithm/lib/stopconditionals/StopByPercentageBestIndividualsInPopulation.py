from typing import List

from geneticAlgorithm.lib.models.Individual import Individual
from geneticAlgorithm.lib.stopconditionals.StopConditional import StopConditional
from geneticAlgorithm.lib.validators.ProbabilityValidator import ProbabilityValidator


class StopByPercentageBestIndividualsInPopulation(StopConditional):

    def __init__(self, percentage_the_best_individuals: float):
        super().__init__()
        ProbabilityValidator.validation(percentage_the_best_individuals, 'percentage_the_best_individuals')
        self.__percentage_the_best_individuals = percentage_the_best_individuals

    def can_stop(self) -> bool:
        can_stop = False
        if self.state is not None:
            population = self.state.population
            population_sorted_by_adaptation = sorted(population,
                                                     key=lambda individual: individual.value_of_adaptation)
            population_sorted_by_adaptation.reverse()
            size_of_population = len(population)
            the_best_individual = population_sorted_by_adaptation[size_of_population - 1]
            the_best_value_adaptation = the_best_individual.value_of_adaptation
            number_the_best = StopByPercentageBestIndividualsInPopulation.__count_best_individuals(
                population_sorted_by_adaptation,
                the_best_value_adaptation)
            percentage_the_best_individuals = number_the_best / len(population)
            if percentage_the_best_individuals >= self.__percentage_the_best_individuals:
                message = 'Achieved ' + str(percentage_the_best_individuals * 100) + "% the best individuals after"\
                          + str(self.state.number_of_cycle) + " cycles" \
                          + "The best founded value adaption: " + str(the_best_value_adaptation)
                print(message)
                can_stop = True

        return can_stop

    @staticmethod
    def __count_best_individuals(population_sorted_by_adaptation: List[Individual],
                                 the_best_value_adaption: float) -> int:
        number_the_best = 0
        for individual in population_sorted_by_adaptation:
            if individual.value_of_adaptation == the_best_value_adaption:
                number_the_best += 1
        return number_the_best
