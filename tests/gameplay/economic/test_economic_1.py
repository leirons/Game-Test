# Positive
# content of test_economic_1.py


from pytest_bdd import scenario, given, then, when
from tests.models.board import Board
from tests.models.indicator import Indicator
from tests.models.pause import Pause
from random import randrange


@scenario('economic.feature', 'Getting n coins for placing a house')
def test_coins_1():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@when("User puts the house of random lvl on cell", target_fixture="user_house")
def user_houses():
    board = Board()
    board.create_custom_board([0, 0, 0, 0])
    board = board.get_board()
    house = (randrange(1, 10))
    board[0] = house
    return house


@then("User gets n coins")
def get_coins(user_house):
    indicator = Indicator()
    coins = indicator.set_house(user_house)
    assert coins == user_house
