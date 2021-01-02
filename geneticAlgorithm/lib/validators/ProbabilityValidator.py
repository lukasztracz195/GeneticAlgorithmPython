class ProbabilityValidator:

    @classmethod
    def validation(cls, probability, probability_name):
        text = str('Invalid Value probability of ' + probability_name)
        assert probability <= 1.0 or probability >= 0.0, text
