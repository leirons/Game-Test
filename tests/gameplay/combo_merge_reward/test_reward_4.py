# content of test_reward_4.py
# Negative test

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.pause import Pause


@scenario("merge_reward.feature", "Try to use crystal at lvl 10 house")
def test_destruction_4():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause
    return {"game_progress": True}


@given("A crystal after combo-merge case", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@given("Board with level 10 house", target_fixture="game_board")
def game_board():
    board = Board()
    board.create_custom_board([10, 0, 0, 0, 0, 0])
    return {"game_board": board}


@when("User drags the crystal to any house level 10", target_fixture="drag_crystal")
def drag_crystal():
    return {"crystal_is_dragged": True}


@then("Nothing will happen")
def increase_lvl(game_board, crystal, drag_crystal):
    increased = False
    is_dragged = drag_crystal.get("crystal_is_dragged")
    assert is_dragged is True
    board = game_board.get("game_board").get_board()
    crystal = crystal.get("crystal")
    assert board is not []
    assert crystal is True
    current_lvl = board[0]
    assert current_lvl != 11
    assert current_lvl == board[0]
    assert crystal is True
    assert increased is False
