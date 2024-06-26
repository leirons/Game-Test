# content of test_board_1.py
# Positive test

from utils.get_root import get_root

import yaml
from pytest_bdd import given, parsers, scenario, then, when


@scenario("board.feature", "User puts the house at empty cell")
def test_board_1():
    pass


EXTRA_TYPES = {"Yml": str, "List": str}



@given(
    parsers.cfparse(
        "Game board with default preset houses {file:Yml}", extra_types=EXTRA_TYPES
    ),
    target_fixture="game_board",
)
def game_board(file,load_fixture_data):

    path = get_root(file)
    data = load_fixture_data(path)
    return data

@given(
    parsers.cfparse("User have in board queue {data:List}", extra_types=EXTRA_TYPES),
    target_fixture="spawn_queue",
)
def spawn_queue(data):
    raw_data = data[1:-1].split(",")

    data = [int(i) for i in raw_data]
    return {"spawn_queue": data}


@when(
    parsers.cfparse("User place on {data:List}", extra_types=EXTRA_TYPES),
    target_fixture="game_data",
)
def user_place(data, game_board, spawn_queue):
    raw_data = data[1:-1].split(",")

    user_place = [int(i) for i in raw_data]

    x, y = user_place
    board = game_board.get("board")
    spawn_queue = spawn_queue.get("spawn_queue")
    house = spawn_queue[3]
    assert house == spawn_queue[3]
    board[x][y] = house
    assert board[x][y] == house
    return [board, user_place, house]


@then(
    parsers.cfparse(
        "A new {file:Yml} should  be generated by user as a result of the installation of the house at empty cell",
        extra_types=EXTRA_TYPES,
    ),
    target_fixture="result_board",
)
def result(file, game_data,load_fixture_data):
    path = get_root(file)
    data = load_fixture_data(path)

    result_board = data.get("board")
    board = game_data[0]
    user_place = game_data[1]
    house = game_data[2]
    x, y = user_place
    assert board == result_board
    assert result_board[x][y] == house
