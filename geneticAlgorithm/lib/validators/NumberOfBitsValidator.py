
class NumberOfBitsValidator:

    @classmethod
    def validation(cls ,number_bits_for_event ,name_of_event, max_value_of_bits ):
        message_1 = str("Number of bits for " + name_of_event + " have to be positive number")
        assert number_bits_for_event > 0, message_1
        message_2 = str("Number of bits cn't be bigger than max value_of_bits = " + str(max_value_of_bits))
        assert number_bits_for_event <= max_value_of_bits, message_2
