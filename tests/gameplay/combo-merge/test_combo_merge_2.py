# content of test_combo_merge_2.py
# Negative test

import yaml
from pytest_bdd import given, parsers, scenario, then, when

from utils.get_root import get_root


@scenario(
    "combo-merge.feature",
    "Negative test to check the impossibility of combo-merging houses of different lvl",
)
def test_combo_merge_2():
    pass


EXTRA_TYPES = {
    "result_house": int,
    "initial_house": int,
    "Yml": str,
    "List": str,
    "Number": int,
}



@given(
    parsers.cfparse(
        "Game board with default preset houses {file:Yml}", extra_types=EXTRA_TYPES
    ),
    target_fixture="game_board",
)
def game_board(file):
    path = get_root(file)
    with open(path) as stream:
        data = yaml.safe_load(stream)
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

    assert board[x][y] == 0
    assert house == spawn_queue[3]
    board[x][y] = house
    assert board[x][y] == house
    return [board, user_place, house]


@then(
    parsers.cfparse(
        "From house lvl {initial_house:Number} should not be generated a new {file:Yml} with combo-merge result lvl {result_house:Number} house",
        extra_types=EXTRA_TYPES,
    ),
    target_fixture="result_board",
)
def result(file, initial_house, result_house, game_data):
    path = get_root(file)
    with open(path) as stream:
        data = yaml.safe_load(stream)


    result_board = data.get("board")
    house = game_data[2]
    user_place = game_data[1]
    board = game_data[0]
    x, y = user_place
    assert board[x][y] == house
    assert board == result_board
    assert result_board[x][y] != result_house
