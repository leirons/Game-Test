# content of test_destruction_1.py
# Positive test
from random import randrange

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.pause import Pause


@scenario("destructing.feature", "Using the destruction function at home")
def test_destruction_1():
    pass

@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [3, 4, 5, 6, 7, 8, 9]
    return board


@given(
    "One possibility to use the destruction function",
    target_fixture="destruction_ability",
)
def destruction_ability():
    return {"destruction": 1}


@when("User destroys a random house", target_fixture="destroyed_house")
def destroyed_house(game_table):
    board = game_table
    house = randrange(1, 10)
    board[0] = house

    board[0] = 0
    assert board[0] == 0
    return True


@then("The house disappears from the game table")
def house_disappear(destroyed_house):
    assert destroyed_house is True


@then("From user takes one possibility to destruction")
def step_impl(destruction_ability):
    ability = destruction_ability.get("destruction")
    ability = ability - 1
    assert ability == 0
