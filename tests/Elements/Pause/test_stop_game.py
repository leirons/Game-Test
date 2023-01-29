# content of test_stop_game.py

from pytest_bdd import scenario, given, then, when
from tests.models.pause import Pause
from random import randrange


@scenario('features/stop_game.feature', 'Pressing the pause button to stop game')
def test_stop_game():
    pass


@given('Game in progress', target_fixture='game_in_progress')
def game_in_progress():
    return {'progress': True, 'pause': Pause()}


@when("The user press on the pause button")
def stop_game(game_in_progress):
    return game_in_progress.get('pause').stop_game()


@then("The game stops and a menu will appear with this elements  <- [tooltip,amount_of_money,record_amount_of_money]")
def stop_game(game_in_progress):
    pause = game_in_progress.get('pause')
    elements = game_in_progress.get('pause').elements
    assert elements[0] == 'tooltip'
    assert elements[1] == 'amount_of_money'
    assert elements[2] == 'record_amount_of_money'
    assert pause.active_pause is False
