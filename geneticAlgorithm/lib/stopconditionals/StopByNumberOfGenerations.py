from geneticAlgorithm.lib.stopconditionals.StopConditional import StopConditional


class StopByNumberOfGenerations(StopConditional):

    def __init__(self, number_of_generation_to_stop: int):
        super().__init__()
        self.__number_of_generation_to_stop = number_of_generation_to_stop

    def can_stop(self) -> bool:
        can_stop = False
        if self.state is not None:
            if self.state.number_of_cycle >= self.__number_of_generation_to_stop:
                print("Stop by achieve expected number of generation, number_of_generation = ",
                      str(self.state.number_of_cycle))
                can_stop = True
        return can_stop

