# Positive
# content of test_economic_3.py

from pytest_bdd import scenario, given, then, when
from tests.models.indicator import Indicator
from tests.models.pause import Pause
from random import randrange


@scenario('economic.feature', 'Getting n*x coins for merging x houses of n lvl')
def test_coins_3():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    return "board"


@when("User merges x houses of n lvl", target_fixture="user_houses")
def user_houses(game_table):
    houses = randrange(3, 9)
    lvl = randrange(1, 10)
    return [houses, lvl]


@then("User gets n*x coins")
def get_coins(user_houses):
    indicator = Indicator()
    n, x = user_houses
    coins = indicator.merged_houses(n, x)
    assert coins == n * x
