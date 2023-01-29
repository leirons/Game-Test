# content of test_gb_1.py

from pytest_bdd import scenario, given, then
from tests.models.board import Board


@scenario('game_board.feature', 'Checking the generation of the game board with positive values')
def test_generation_with_positive_values():
    pass


@given(
    "Game board with positive generated values", target_fixture="game_board")
def game_board():
    board = Board()
    board.generate_positive_board()
    return board


@then("User must see the game board")
def check_game_board(game_board):
    board = game_board.get_board()
    passed = True
    for i in board:
        if len(i) != 6:
            passed = False
    if len(board) != 6:
        passed = False
    assert passed is True
