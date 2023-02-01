# content of test_reward_1.py
# Positive test

import yaml
from pytest_bdd import scenario, given, then, when, parsers

from models.pause import Pause


@scenario('board.feature', 'User puts the house at empty cell')
def test_board_1():
    pass


EXTRA_TYPES = {
    'Yml': str,
    "List": str
}


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@given(parsers.cfparse('Game board with default preset houses {file:Yml}', extra_types=EXTRA_TYPES),
       target_fixture='game_board')
def game_board(file):
    with open("board/positive/default.yml", "r") as stream:
        data = yaml.safe_load(stream)
        return data


@given(parsers.cfparse('User have in board queue {data:List}', extra_types=EXTRA_TYPES),
       target_fixture='spawn_queue')
def spawn_queue(data):
    raw_data = data[1:-1].split(',')

    data = [int(i) for i in raw_data]
    return {"spawn_queue": data}


@when(parsers.cfparse('User place on {file:Yml}', extra_types=EXTRA_TYPES),
      target_fixture='game_data')
def user_place(file, game_board, spawn_queue):
    with open(file, "r") as stream:
        data = yaml.safe_load(stream)
    user_place = data.get('user_place')
    x, y = user_place
    board = game_board.get('board')
    spawn_queue = spawn_queue.get('spawn_queue')
    house = spawn_queue[3]
    assert house == spawn_queue[3]
    board[x][y] = house
    assert board[x][y] == house
    return [board, user_place, house]


@then(parsers.cfparse(
    'A new {file:Yml} should  be generated by user as a result of the installation of the house at empty cell',
    extra_types=EXTRA_TYPES),
    target_fixture='result_board')
def result(file, game_data):
    with open(file, "r") as stream:
        data = yaml.safe_load(stream)
    result_board = data.get('board')
    board = game_data[0]
    user_place = game_data[1]
    house = game_data[2]
    x, y = user_place
    assert board == result_board
    assert result_board[x][y] == house
