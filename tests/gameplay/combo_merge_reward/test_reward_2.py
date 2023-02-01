# content of test_reward_2.py
# Positive test

from pytest_bdd import scenario, given, then, when, parsers

from models.board import Board
from models.pause import Pause

EXTRA_TYPES = {
    'List': str,
    "Number": int
}


@scenario('merge_reward.feature', 'Checking house returns to initial position at spawn place after using crystal')
def test_reward_2():
    pass


@given(parsers.cfparse('Spawn queue {data:List} with {number:Number} in cache', extra_types=EXTRA_TYPES),
       target_fixture='spawn_queue')
def spawn_queue(data, number):
    data = data[1:-1].split(',')

    return {"spawn_queue": data, "cache_house": number}


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@given("A crystal after combo-merge case", target_fixture="crystal")
def crystal():
    return {'crystal': True}


@given("Board with houses up to level 9", target_fixture="game_board")
def game_board():
    board = Board()
    board.create_custom_board([3, 5, 6, 7, 4, 5])
    return {"game_board": board}


@when("User drags the crystal to any house up to level 9", target_fixture="drag_crystal")
def drag_crystal():
    return {'crystal_is_dragged': True}


@then(parsers.cfparse('User gets house with lvl {result_from_cache:Number} from cache', extra_types=EXTRA_TYPES))
def increase_lvl(spawn_queue,crystal, result_from_cache, game_board, drag_crystal):
    increased = True

    is_dragged = drag_crystal.get('crystal_is_dragged')
    queue = spawn_queue.get("spawn_queue")
    cache_house = spawn_queue.get("cache_house")
    assert is_dragged is True
    board = game_board.get('game_board').get_board()
    crystal = crystal.get("crystal")
    assert board is not []
    assert crystal is True
    current_lvl = board[0]
    updated_lvl = current_lvl + 1
    assert updated_lvl > current_lvl
    assert updated_lvl - 1 == current_lvl
    assert updated_lvl != 11
    crystal = False
    assert result_from_cache == cache_house
    new_spawn = [result_from_cache]
    for i in range(3):
        new_spawn.append(queue[i])
    assert new_spawn[3] == queue[2]
    assert new_spawn[0] == cache_house
    assert increased is True
    assert crystal is False

