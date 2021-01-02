import unittest
from geneticAlgorithm.lib.models.Individual import Individual


class MyTestCase(unittest.TestCase):

    def test_set_positive_fields_in_object_individual(self):
        phenotype_x = 2.5
        phenotype_y = 3.75
        individual = Individual(phenotype_x, phenotype_y)
        self.assertEqual(individual.get_x_phenotype(), phenotype_x, "Phenotype is not valid, should be {0}".format(phenotype_x))
        self.assertEqual(individual.get_y_phenotype() == phenotype_y, "Phenotype is not valid, should be {0}".format(phenotype_y))
        SIGN_BIT_EXPECTED_GENOTYPE_X = [0]
        BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_X = [0, 1, 0]
        BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_X = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0]
        EXPECTED_GENOTYPE_X = SIGN_BIT_EXPECTED_GENOTYPE_X + BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_X + \
                              BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_X
        self.assertEqual(v, EXPECTED_GENOTYPE_X, "Genotype is not valid, should be {0} but was {1}".format(EXPECTED_GENOTYPE_X, )

        SIGN_BIT_EXPECTED_GENOTYPE_Y = [0]
        BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_Y = [0, 1, 1]
        BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_Y = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0]
        EXPECTED_GENOTYPE_Y = SIGN_BIT_EXPECTED_GENOTYPE_Y + BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_Y + \
                              BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_Y
        assert individual.get_y_genotype() == EXPECTED_GENOTYPE_Y, "Genotype is not valid"

        assert individual.get_probability_of_selection() == 0, "Invalid probability selection of value"
        assert individual.get_start() == 0, "Invalid start of value"
        assert individual.get_stop() == 0, "Invalid stop of value"
        assert individual.get_value_adaption() == 0, "Invalid value adaptation of value"

    def test_set_negative_fields_in_object_individual(self):
        individual = Individual(-2.5, -3.75)
        assert individual.get_x_phenotype() == -2.5, "Phenotype is not valid"
        assert individual.get_y_phenotype() == -3.75, "Phenotype is not valid"

        SIGN_BIT_EXPECTED_GENOTYPE_X = [1]
        BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_X = [0, 1, 0]
        BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_X = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0]
        EXPECTED_GENOTYPE_X = SIGN_BIT_EXPECTED_GENOTYPE_X + BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_X + \
                              BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_X
        assert individual.get_x_genotype() == EXPECTED_GENOTYPE_X, "Genotype is not valid"

        SIGN_BIT_EXPECTED_GENOTYPE_Y = [1]
        BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_Y = [0, 1, 1]
        BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_Y = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0]
        EXPECTED_GENOTYPE_Y = SIGN_BIT_EXPECTED_GENOTYPE_Y + BITS_ON_INTEGER_PART_EXPECTED_GENOTYPE_Y + \
                              BITS_ON_FLOATING_PART_EXPECTED_GENOTYPE_Y
        assert individual.get_y_genotype() == EXPECTED_GENOTYPE_Y, "Genotype is not valid"

        assert individual.get_probability_of_selection() == 0, "Invalid probability selection of value"
        assert individual.get_start() == 0, "Invalid start of value"
        assert individual.get_stop() == 0, "Invalid stop of value"
        assert individual.get_value_adaption() == 0, "Invalid value adaptation of value"


if __name__ == '__main__':
    unittest.main()
