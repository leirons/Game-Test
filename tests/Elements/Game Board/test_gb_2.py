# content of test_gb_2.py

from pytest_bdd import scenario, given, then

from models.board import Board


@scenario('game_board.feature', 'Checking the generation of the game board with negative values')
def test_generation_with_negative_values():
    pass


@given(
    "Game board with negative generated values", target_fixture="game_board")
def game_board():
    board = Board()
    board.generate_negative_board()
    return board


@then("The game board should be recreated")
def check_game_board(game_board):
    board = game_board.get_board()
    passed = True
    for i in board:
        if len(i) != 6:
            passed = False
    if len(board) != 6:
        passed = False
    assert passed is True
