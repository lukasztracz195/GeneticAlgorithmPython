from geneticAlgorithm import GeneticAlgorithm


class StopConditional():

    def __init__(self):
        self.state = None

    def can_stop(self) -> bool:
        """Overrides StopConditional.can_stop()"""
        pass

    def update_state(self, state: GeneticAlgorithm):
        self.state = state
