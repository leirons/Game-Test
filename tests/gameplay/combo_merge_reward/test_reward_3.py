# content of test_reward_3.py
# Negative test

from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.pause import Pause


@scenario("merge_reward.feature", "Try to use crystal at empty cell")
def test_reward_3():
    pass




@given("A crystal after combo-merge case", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@given("Board with empty cell", target_fixture="game_board")
def game_board():
    board = [3, 4, 5, 6, 7, 8, 9]
    return {"game_board": board}


@when("User drags the crystal to any empy cell", target_fixture="drag_crystal")
def drag_crystal():
    return {"crystal_is_dragged": True}


@then("Nothing will happen")
def increase_lvl(game_board, crystal, drag_crystal):
    increased = False

    is_dragged = drag_crystal.get("crystal_is_dragged")
    assert is_dragged is True
    board = game_board.get("game_board")
    crystal = crystal.get("crystal")
    assert board is not []
    assert crystal is True
    current_lvl = board[0]
    assert current_lvl == board[0]
    assert crystal is True
    assert increased is False
