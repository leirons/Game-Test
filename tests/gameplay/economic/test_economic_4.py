# Positive
# content of test_economic_4.py

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.indicator import Indicator
from game.models.pause import Pause


@scenario("economic.feature", "Getting n+1 coins for using crystal")
def test_coins_4():
    pass

@given("Crystal", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [3, 4, 5, 6, 7, 8, 9]
    return board


@when("User use crystal on a house", target_fixture="user_houses")
def user_houses(crystal, game_table):
    assert crystal.get("crystal") is True
    board = game_table
    coordinate = 1
    assert coordinate == 1
    return board[coordinate]


@then("User gets n+1 coins")
def get_coins(user_houses):
    indicator = Indicator()
    n = user_houses
    coins = indicator.used_crystal(n)
    assert coins == n + 1
