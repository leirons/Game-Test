# Positive
# content of test_economic_2.py

from pytest_bdd import scenario, given, then, when
from tests.models.board import Board
from tests.models.indicator import Indicator
from tests.models.pause import Pause
from random import randrange


@scenario('economic.feature', 'Getting n*20 coins for destroying a house')
def test_coins_2():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}

@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = Board()
    board.create_custom_board([0, 0, 0, 0])
    board = board.get_board()
    return board


@when("User destroys a random house", target_fixture="destroyed_house")
def destroyed_house(game_table):
    board = game_table
    house = (randrange(1, 10))
    board[0] = house

    board[0] = 0
    assert board[0] == 0
    return house


@then("User gets n*20 coins")
def get_coins(destroyed_house):
    indicator = Indicator()
    coins = indicator.destroyed_house(destroyed_house)
    assert coins == destroyed_house * 20
