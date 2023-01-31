# content of test_probability_3.py
# Positive test

import random

import yaml
from pytest_bdd import scenario, given, then, when, parsers


@scenario('probability.feature', 'Level 3 probability test')
def test_probability_3():
    pass


EXTRA_TYPES = {
    'Yml': str,
}


@given(parsers.cfparse('A {file:Yml} with probability chances', extra_types=EXTRA_TYPES),
       target_fixture='probability_chances')
def probability_chances(file):
    with open(file, "r") as stream:
        data = yaml.safe_load(stream)
        return data


@given("Game board with max house lvl 3")
def game_board():
    """Not implemented"""
    pass


@when("User place a house on game board")
def user_place():
    """Not implemented"""
    pass


@then("The user gets a house on the spawn board with a certain probability chance")
def check_probability(probability_chances):
    probabilities = probability_chances.get('probabilities')
    chances = probabilities.get(3)
    houses = [i for i in range(len(chances))]
    result = random.choices(houses, weights=chances, k=1)[0]
    assert result in houses
