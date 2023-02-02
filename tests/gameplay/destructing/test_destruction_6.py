# content of test_destruction_6.py
# Negative test

from random import randrange

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.pause import Pause


@scenario("destructing.feature", "Using the destruction function at spawn place")
def test_destruction_6():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause is True
    return {"game_progress": True}


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = Board()
    board.create_custom_board([0, 0, 0, 0])
    board = board.get_board()
    return board


@given(
    "One possibility to use the destruction function",
    target_fixture="destruction_ability",
)
def destruction_ability():
    return {"destruction": 1}


@given("Spawn board with random lvl of houses", target_fixture="spawn_board")
def spawn_board():
    spawn_board = []
    for i in range(4):
        spawn_board.append(randrange(1, 10))

    return {"spawn_board": spawn_board}


@when("User try to destroy a house on spawn cell", target_fixture="destroyed_house")
def destroyed_house(spawn_board):
    assert len(spawn_board.get("spawn_board")) == 4
    for i in spawn_board:
        assert i != 0
    return False


@then("Nothing will happen")
def house(destroyed_house):
    assert destroyed_house is False


@then("From user wont take one possibility to destruction")
def check_ability(destruction_ability):
    ability = destruction_ability.get("destruction")
    assert ability == 1
