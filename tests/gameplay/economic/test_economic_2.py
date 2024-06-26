# Positive
# content of test_economic_2.py

from random import randrange

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.indicator import Indicator
from game.models.pause import Pause


@scenario("economic.feature", "Getting n*20 coins for destroying a house")
def test_coins_2():
    pass

@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [3, 4, 5, 6, 7, 8, 9]
    return board


@when("User destroys a random house", target_fixture="destroyed_house")
def destroyed_house(game_table):
    board = game_table
    house = randrange(1, 10)
    board[0] = house

    board[0] = 0
    assert board[0] == 0
    return house


@then("User gets n*20 coins")
def get_coins(destroyed_house):
    indicator = Indicator()
    coins = indicator.destroyed_house(destroyed_house)
    assert coins == destroyed_house * 20
