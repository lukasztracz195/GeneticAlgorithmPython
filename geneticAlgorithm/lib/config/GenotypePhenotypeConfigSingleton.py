import math

from geneticAlgorithm.lib.config.SingletonMeta import SingletonMeta


class GenotypePhenotypeConfigSingleton(metaclass=SingletonMeta):
    __bit_sign = 0
    __number_of_bits_on_integer_part = None
    __number_of_bits_on_floating_part = None
    __min_phenotype_value = None
    __max_phenotype_value = None

    @property
    def bit_sign(self) -> int:
        return self.__bit_sign

    @property
    def number_of_bits_on_integer_part(self) -> int:
        return self.__number_of_bits_on_integer_part

    @number_of_bits_on_integer_part.setter
    def number_of_bits_on_integer_part(self, value: int):
        self.__number_of_bits_on_integer_part = value

    @property
    def number_of_bits_on_floating_part(self) -> int:
        return self.__number_of_bits_on_floating_part

    @number_of_bits_on_floating_part.setter
    def number_of_bits_on_floating_part(self, value: int):
        self.__number_of_bits_on_floating_part = value

    @property
    def min_phenotype_value(self) -> float:
        return self.__min_phenotype_value

    @min_phenotype_value.setter
    def min_phenotype_value(self, value: float):
        self.__min_phenotype_value = value

    @property
    def max_phenotype_value(self) -> float:
        return self.__max_phenotype_value

    @max_phenotype_value.setter
    def max_phenotype_value(self, value: float):
        self.__max_phenotype_value = value

    @property
    def number_of_bits_for_genotype(self) -> int:
        return 1 + self.__number_of_bits_on_integer_part + self.__number_of_bits_on_floating_part

    @number_of_bits_on_integer_part.setter
    def number_of_bits_on_integer_part(self, value):
        self.__number_of_bits_on_integer_part = value

    @number_of_bits_on_floating_part.setter
    def number_of_bits_on_floating_part(self, value):
        self.__number_of_bits_on_floating_part = value

    def set_and_count_number_of_bits_to_write_integer(self):
        list_values = [abs(self.max_phenotype_value), abs(self.__min_phenotype_value)]
        value_max = max(list_values)
        exponent_bit = 0
        number_bits = 1
        while True:
            value = math.pow(2, exponent_bit)
            if value < value_max:
                exponent_bit += 1
                number_bits += 1
            else:
                break
        self.__number_of_bits_on_integer_part = number_bits-1
