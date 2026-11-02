# content of test_board_2.py
# Positive test

import yaml
from pytest_bdd import given, parsers, scenario, then, when

from utils.get_root import get_root


@scenario("board.feature", "User puts the house at used cell")
def test_board_2():
    pass


EXTRA_TYPES = {"Yml": str, "List": str}


@given(
    parsers.cfparse(
        "Game board with default preset houses {file:Yml}", extra_types=EXTRA_TYPES
    ),
    target_fixture="game_board",
)
def game_board(file, load_fixture_data):
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

    assert board[x][y] != 0
    return ""


@then("Nothing will happen")
def result(game_data):
    """Not implemented"""
    pass
