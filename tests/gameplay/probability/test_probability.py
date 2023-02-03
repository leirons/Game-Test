# content of test_probability.py
# Positive test

import random

import yaml
from pytest_bdd import given, parsers,then, when, scenarios

from utils.get_root import get_root

scenarios("probability.feature")

EXTRA_TYPES = {
    "Yml": str,
    "d": int
}


@given(
    parsers.cfparse("A {file:Yml} with probability chances", extra_types=EXTRA_TYPES),
    target_fixture="probability_chances",
)
def probability_chances(file,load_fixture_data):
    path = get_root(file)
    data = load_fixture_data(path)
    return data


@given(parsers.parse("Game board with max house {lvl:d}"), target_fixture="lvl")
def game_board(lvl):
    return lvl


@when("User place a house on game board")
def user_place():
    """Not implemented"""
    pass


@then("The user gets a house on the spawn board with a certain probability chance")
def check_probability(probability_chances, lvl):
    probabilities = probability_chances.get("probabilities")
    chances = probabilities.get(lvl)
    houses = [i for i in range(1, len(chances) + 1)]
    result = random.choices(houses, weights=chances, k=1)[0]
    assert result in houses
