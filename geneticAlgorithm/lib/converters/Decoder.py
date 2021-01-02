from typing import List

from geneticAlgorithm.lib.config.GenotypePhenotypeConfigSingleton import GenotypePhenotypeConfigSingleton


class Decoder(GenotypePhenotypeConfigSingleton):

    @classmethod
    def decode(cls, genotype: List[int]) -> float:
        assert len(genotype) == GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype,\
            "Can't decode genotype, by wrong number of bits"
        sign_multiplier = Decoder.__get_value_for_sign_bit(genotype)
        integer_part = Decoder.__get_value_from_integer_part(genotype)
        floating_part = Decoder.__get_value_from_floating_part(genotype)
        return sign_multiplier * (integer_part + floating_part)

    @classmethod
    def __get_value_for_sign_bit(cls, genotype: List[int]):
        if genotype[GenotypePhenotypeConfigSingleton().bit_sign] == 0:
            return 1
        else:
            return -1

    @classmethod
    def __get_value_from_integer_part(cls, genotype) -> int:
        integer_part = 0
        index = 1
        for exponent in Decoder.__generate_list_exponents_for_integer_part():
            integer_part += pow(2, exponent) * genotype[index]
            index += 1
        return integer_part

    @classmethod
    def __get_value_from_floating_part(cls, genotype) -> float:
        floating_part = 0.0
        index = GenotypePhenotypeConfigSingleton().number_of_bits_for_genotype - GenotypePhenotypeConfigSingleton().number_of_bits_on_floating_part
        list_exponents_for_floating_part = Decoder.__generate_list_exponents_for_floating_part()
        for exponent in list_exponents_for_floating_part:
            floating_part += pow(2, exponent) * genotype[index]
            index += 1
        return floating_part

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