# content of test_board_4.py
# Positive test


from pytest_bdd import given, scenario, then,when


@scenario(
    "board.feature", "The user is trying to change the position of the already placed house"
)
def test_board_4():
    pass


@given("Given Random numbers of houses on the game table", target_fixture="game_board")
def game_board():
    return [1, 4, 3, 2, 1]


def change_position(game_board, house):
    return False


@when("The user tries to drag the house to another position")
def putting_house_on_another_position(game_board):
    initial_game_board = game_board
    result_game_board = game_board
    assert change_position(game_board, game_board[0]) is False
    assert initial_game_board == result_game_board


@then("Nothing will happen")
def result(game_board):
    pass
