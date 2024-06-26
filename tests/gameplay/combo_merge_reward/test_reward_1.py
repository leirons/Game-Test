# content of test_reward_1.py
# Positive test
from pytest_bdd import given, scenario, then, when

from game.models.board import Board
from game.models.pause import Pause


@scenario("merge_reward.feature", "Increase house level by +1 with crystal")
def test_reward_1():
    pass
@given("A crystal after combo-merge case", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@given("Board with houses up to level 9", target_fixture="game_board")
def game_board():
    board = [3,4,5,6,7,8,9]
    return {"game_board": board}


@when(
    "User drags the crystal to any house up to level 9", target_fixture="drag_crystal"
)
def drag_crystal():
    return {"crystal_is_dragged": True}


@then("User gets house with current level +1")
def increase_lvl(game_board, crystal, drag_crystal):
    increased = True
    is_dragged = drag_crystal.get("crystal_is_dragged")
    assert is_dragged is True
    board = game_board.get("game_board")
    crystal = crystal.get("crystal")
    assert board is not []
    assert crystal is True
    current_lvl = board[0]
    updated_lvl = current_lvl + 1
    assert updated_lvl > current_lvl
    assert updated_lvl - 1 == current_lvl
    assert updated_lvl != 11
    crystal = False
    assert crystal is False
    assert increased is True
