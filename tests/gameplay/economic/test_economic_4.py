# Positive
# content of test_economic_4.py

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.indicator import Indicator
from game.models.pause import Pause


@scenario("economic.feature", "Getting n+1 coins for using crystal")
def test_coins_4():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause
    return {"game_progress": True}


@given("Crystal", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = Board()
    board.create_custom_board([0, 3, 0, 0])
    return board


@when("User use crystal on a house", target_fixture="user_houses")
def user_houses(crystal, game_table):
    assert crystal.get("crystal") is True
    board = game_table
    coordinate = 1
    result = board.use_crystal(coordinate)
    assert result is True
    return board.get_board()[coordinate]


@then("User gets n+1 coins")
def get_coins(user_houses):
    indicator = Indicator()
    n = user_houses
    coins = indicator.used_crystal(n)
    assert coins == n + 1
