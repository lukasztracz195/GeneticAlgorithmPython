import matplotlib.pyplot as plt
import numpy as np

from geneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from geneticAlgorithm.fun.ConcreteFunction import ConcreteFunction
from geneticAlgorithm.lib.config.ConfigGeneticAlgorithm import ConfigGeneticAlgorithm
from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton
from geneticAlgorithm.lib.selection.RankedSelection import RankedSelection

# Skonfigurowanie kodowania genotypu
from geneticAlgorithm.lib.selection.RouletteWheelSelection import RouletteWheelSelection
from geneticAlgorithm.lib.stopconditionals.StopByAchieveValueFunction import StopByAchieveValueFunction
from geneticAlgorithm.lib.stopconditionals.StopByPercentageBestIndividualsInPopulation import \
    StopByPercentageBestIndividualsInPopulation

config_genotype_phenotype = GenotypePhenotypeConfigSingleton()
config_genotype_phenotype.min_phenotype_value = -8
config_genotype_phenotype.max_phenotype_value = 8
config_genotype_phenotype.set_and_count_number_of_bits_to_write_integer()
config_genotype_phenotype.number_of_bits_on_floating_part = 28

# Przygotowanie konfiguracji algorytmu genetycznego
config_genetic_algorithm = ConfigGeneticAlgorithm(probability_of_crossing=0.8,
                                                  number_points_to_crossing=4,
                                                  probability_of_mutation=0.05,
                                                  number_points_to_mutation=1,
                                                  size_of_population=1000)

# Określenie warunku stopu
# stop_condition = StopByNumberOfGenerations(number_of_generation_to_stop=100)
# stop_condition = StopByPercentageBestIndividualsInPopulation(percentage_the_best_individuals=0.95)
stop_condition = StopByAchieveValueFunction(value_function_to_stop=256.0, epsilon=0.01)


# Utworzenie obiektu funkcji celu potrzebnego do
function = ConcreteFunction()

# Wybranie algorytmu do selekcji
selection_algorithm = RouletteWheelSelection()
# selection_algorithm = RankedSelection(number_of_individuals_to_swap=50)

# Utworzenie instancji algorytmu gentycznego
genetic_algorithm = GeneticAlgorithm(config=config_genetic_algorithm,
                                     stop_condition=stop_condition,
                                     function=function,
                                     selection_algorithm=selection_algorithm,
                                     debug=True)

# Uruchomienie symulacji
genetic_algorithm.start()

history = genetic_algorithm.history_max_value_adaption

x = np.arange(0, len(history))
plt.plot(x, history)
plt.xlabel('Number of generations')
plt.ylabel('Value adaption of the best individual from population')
plt.show()
