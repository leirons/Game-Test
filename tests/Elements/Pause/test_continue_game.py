# content of test_stop_game.py

from pytest_bdd import scenario, given, then, when
from tests.models.pause import Pause


@scenario('features/continue_game.feature', 'Pressing the continue game button to continue the game')
def test_continue_game():
    pass


@given('Game in progress', target_fixture='game_in_progress')
@given("The game is paused")
def game_in_progress():
    pause = Pause()
    pause.stop_game()
    return {'progress': True, 'pause': Pause()}


@when("The user press on continue button")
def continue_game(game_in_progress):
    return game_in_progress.get('pause').continue_game()


@then("The game will continue")
def stop_game(game_in_progress):
    pause = game_in_progress.get('pause')
    assert pause.active_pause is True
