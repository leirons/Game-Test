# Positive
# content of test_economic_1.py


from random import randrange

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.indicator import Indicator
from game.models.pause import Pause


@scenario("economic.feature", "Getting n coins for placing a house")
def test_coins_1():
    pass

@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [3, 4, 5, 6, 7, 8, 9]
    return board


@when("User puts the house of random lvl on cell", target_fixture="user_house")
def user_houses(game_table):
    board = game_table
    house = randrange(1, 10)
    board[0] = house
    return house


@then("User gets n coins")
def get_coins(user_house):
    indicator = Indicator()
    coins = indicator.set_house(user_house)
    assert coins == user_house
