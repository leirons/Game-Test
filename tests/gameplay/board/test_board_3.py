# content of test_board_3.py
# Positive test


from pytest_bdd import given, scenario, then

@scenario(
    "board.feature", "Checking the end of the game after the entire game board is full"
)
def test_board_3():
    pass




@given(
    "Fully filled board with houses of different levels", target_fixture="full_board"
)
def full_board():
    return [
        [1, 2, 10, 9, 1, 5],
        [2, 3, 9, 10, 2, 1],
        [3, 4, 8, 9, 3, 2],
        [4, 5, 6, 5, 4, 5],
        [5, 6, 5, 4, 6, 7],
        [6, 7, 4, 3, 2, 1],
    ]


@then("Game is stopped")
def game_stopped(full_board):
    for i in full_board:
        for j in i:
            assert j != 0
