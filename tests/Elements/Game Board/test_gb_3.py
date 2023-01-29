# content of test_gb_3.py

from pytest_bdd import scenario, given, then

from models.board import Board


@scenario('game_board.feature',
          'Checking the generation of the game board with different number of houses from 0 to 36')
def test_number_of_houses_at_game_board():
    pass


@given(
    "Game board with positive random preset of different number of houses from 0 to 36", target_fixture="game_board")
def game_board():
    board = Board()
    board.create_board_with_different_number_of_houses()
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


@then("The game board must have a generated number of houses")
def check_number_of_houses(game_board):
    board = game_board.get_board()
    number_of_houses = game_board.houses.number_of_houses
    current = 0
    for i in board:
        for j in i:
            if j != 0:
                current = current + 1
    assert current == number_of_houses
