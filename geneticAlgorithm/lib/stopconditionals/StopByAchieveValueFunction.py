from geneticAlgorithm.lib.stopconditionals.StopConditional import StopConditional


class StopByAchieveValueFunction(StopConditional):

    def __init__(self, value_function_to_stop: float, epsilon: float):
        super().__init__()
        self.__value_function_to_stop = value_function_to_stop
        self.__epsilon = epsilon

    def can_stop(self) -> bool:
        can_stop = False
        if self.state is not None:
            population = self.state.population
            for individual in population:
                value_adaption = individual.value_of_adaptation
                accepted_min_value = self.__value_function_to_stop - self.__epsilon
                accepted_max_value = self.__value_function_to_stop + self.__epsilon
                if accepted_min_value <= value_adaption <= accepted_max_value:
                    print("Found individual which accepted criterion value adaption after ", str(self.state.number_of_cycle)," cycle\n")
                    print(individual)
                    can_stop = True
        return can_stop
