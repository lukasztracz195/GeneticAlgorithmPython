from geneticAlgorithm.fun.Function import Function


class ConcreteFunction(Function):

    def __init__(self):
        super().__init__()

    def count_value_function(self) -> float:
        assert self.dictionary_parameters is not None, "Not initialized parameters of function"
        assert self.dictionary_parameters['x'] is not None or self.dictionary_parameters[
            'y'] is not None, "Not initialized parameters of function"
        value = pow(-self.dictionary_parameters['x'], 2) + pow(self.dictionary_parameters['y'], 2) - 2 * \
               self.dictionary_parameters['x'] * self.dictionary_parameters['y']
        return value

    def update_parameters(self, dictionary):
        self.dictionary_parameters = dictionary
