import math
from typing import List

from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton


class Coder(GenotypePhenotypeConfigSingleton):

    @classmethod
    def code(cls, phenotype: float) -> List[int]:
        assert phenotype <= GenotypePhenotypeConfigSingleton().max_phenotype_value, "Value of phenotype is greater than the possible maximum value"
        assert phenotype >= GenotypePhenotypeConfigSingleton().min_phenotype_value, "Value of phenotype is lower than the possible minimal value"
        sign = Coder.__get_value_of_bit_sign(phenotype)
        bits_integer_part = Coder.__get_bits_values_for_integer_parts(phenotype)
        bits_floating_part = Coder.__get_bits_value_for_floating_part(phenotype)
        return sign + bits_integer_part + bits_floating_part

    @classmethod
    def __get_bits_value_for_floating_part(cls, phenotype: float) -> List[int]:
        genotype_list = []
        integer_part = abs(math.floor(abs(phenotype)))
        floating_part = abs(abs(phenotype) - integer_part)
        for exponent in Coder.__generate_list_exponents_for_floating_part():
            devider = math.pow(2, exponent)
            if floating_part == 0:
                value_m = 0
                value_d = 0
            else:
                value_m = devider % floating_part
                value_d = devider / floating_part

            if value_m == 0 and value_d == 1.0:
                bit = 1
            elif value_m > 0 and value_d < 1.0:
                bit = 1
            else:
                bit = 0
            genotype_list.append(bit)
            floating_part = floating_part - (pow(2, exponent) * bit)
        return genotype_list

    @classmethod
    def __get_bits_values_for_integer_parts(cls, phenotype) -> List[int]:
        genotype_list = []
        integer_part = abs(math.floor(abs(phenotype)))
        for exponent in Coder.__generate_list_exponents_for_integer_part():
            p = pow(2, exponent)
            if integer_part > 0:
                value_m = p % integer_part
                value_d = p / integer_part
            else:
                value_m = 0
                value_d = 0
            if value_m == 0 and value_d == 1.0:
                bit = 1
            elif value_m > 0 and value_d < 1.0:
                bit = 1
            else:
                bit = 0
            genotype_list.append(bit)
            integer_part -= (pow(2, exponent)) * bit
        return genotype_list

    @classmethod
    def __generate_list_exponents_for_integer_part(cls) -> List[int]:
        list_exponents = []
        for index in range(GenotypePhenotypeConfigSingleton().number_of_bits_on_integer_part - 1, -1, -1):
            list_exponents.append(index)
        return list_exponents

    @classmethod
    def __generate_list_exponents_for_floating_part(cls) -> List[int]:
        list_exponents = []
        for index in range(-1, -(GenotypePhenotypeConfigSingleton().number_of_bits_on_floating_part + 1), -1):
            list_exponents.append(index)
        return list_exponents

    @classmethod
    def __get_value_of_bit_sign(cls, phenotype) -> List[int]:
        if phenotype > 0:
            return [0]
        else:
            return [1]