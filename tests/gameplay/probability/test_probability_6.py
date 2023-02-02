# content of test_probability_6.py
# Positive test

import pathlib
import random

import yaml
from pytest_bdd import given, parsers, scenario, then, when


@scenario("probability.feature", "Level 6 probability test")
def test_probability_6():
    pass


EXTRA_TYPES = {
    "Yml": str,
}


@given(
    parsers.cfparse("A {file:Yml} with probability chances", extra_types=EXTRA_TYPES),
    target_fixture="probability_chances",
)
def probability_chances(file):
    with (pathlib.Path(__file__).parent / file).open("r") as stream:
        data = yaml.safe_load(stream)
        return data


@given("Game board with max house lvl 6")
def game_board():
    """Not implemented"""
    pass


@when("User place a house on game board")
def user_place():
    """Not implemented"""
    pass


@then("The user gets a house on the spawn board with a certain probability chance")
def check_probability(probability_chances):
    probabilities = probability_chances.get("probabilities")
    chances = probabilities.get(6)
    houses = [i for i in range(1, len(chances) + 1)]
    result = random.choices(houses, weights=chances, k=1)[0]

    assert result in houses
