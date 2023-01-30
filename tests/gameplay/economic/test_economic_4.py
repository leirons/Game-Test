# Positive
# content of test_economic_4.py

from pytest_bdd import scenario, given, then, when
from models.board import Board
from tests.models.indicator import Indicator
from tests.models.pause import Pause


@scenario('economic.feature', 'Getting n+1 coins for using crystal')
def test_coins_4():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@given("Crystal", target_fixture="crystal")
def crystal():
    return {'crystal': True}


@when("User use crystal on a house", target_fixture="user_houses")
def user_houses(crystal):
    assert crystal.get('crystal') is True

    board = Board()
    board.create_custom_board([0, 3, 0, 0])
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
