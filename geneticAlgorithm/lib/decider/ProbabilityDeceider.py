import random


class ProbabilityDecider:

    @classmethod
    def decide_with_probability(cls, probability_of_happening: float):
        assert 0.0 <= probability_of_happening <= 1.0, "Value of probability_of_happening have to from range [0,1]"
        list_possibles = [True, False]
        probability_of_not_happening = 1 - probability_of_happening
        weights = [probability_of_happening,probability_of_not_happening ]
        list_with_decision = random.choices(list_possibles,weights=weights, k=1)
        return list_with_decision[0]