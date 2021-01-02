import random
from typing import List


class BitsRandomizer:

    @classmethod
    def random_without_returning(self, number_of_bits: int, number_of_bits_to_random: int) -> List[int]:
        assert number_of_bits_to_random <= number_of_bits, "Can't random bits, when we set of values to random is to lower than expected drawn bits"
        assert number_of_bits > 0, "Number of bits have to positive number"
        assert number_of_bits_to_random > 0, "Number of bits have to positive number"
        selected_bits = set()
        while (len(selected_bits) < number_of_bits_to_random):
            selected_bit = random.randint(0, number_of_bits - 1)
            if selected_bit in selected_bits:
                pass
            else:
                selected_bits.add(selected_bit)
        return list(selected_bits)

    @classmethod
    def random_with_returning(self, number_of_bits: int, number_of_bits_to_random: int) -> List[int]:
        assert number_of_bits > 0, "Number of bits have to positive number"
        assert number_of_bits_to_random > 0, "Number of bits have to positive number"
        selected_bits = list()
        for i in range(number_of_bits_to_random):
            selected_bit = random.randint(0, number_of_bits - 1)
            selected_bits.append(selected_bit)
        return selected_bits
