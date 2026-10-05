# content of test_board_4.py
# Positive test

from pytest_bdd import given, parsers, scenario, then, when

EXTRA_TYPES = {"Yml": str, "List": str}


@scenario(
    "board.feature",
    "The user is trying to place the house that does not exists in queue",
)
def test_board_4():
    pass


@given("Given Random numbers of houses on the game table", target_fixture="game_board")
def game_board():
    return [1, 4, 3, 2, 1]


@given(
    parsers.cfparse("User have in board queue {data:List}", extra_types=EXTRA_TYPES),
    target_fixture="spawn_queue",
)
def spawn_queue(data):
    raw_data = data[1:-1].split(",")

    data = [int(i) for i in raw_data]
    return {"spawn_queue": data}


@given("House that does not exists in queue", target_fixture="get_house")
def get_house(spawn_queue):
    set_houses = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    houses = spawn_queue.get("spawn_queue")

    house = list(set_houses - set(houses))[1]
    assert house not in houses
    return house


def change_position(game_board, house):
    return False


@when("User try to place a house on random empty place")
def putting_house_on_another_position(game_board, get_house):
    initial_game_board = game_board
    result_game_board = game_board
    house = get_house
    assert change_position(game_board, house) is False
    assert initial_game_board == result_game_board


@then("Nothing will happen")
def result(game_board):
    """Not implemented"""
    pass
