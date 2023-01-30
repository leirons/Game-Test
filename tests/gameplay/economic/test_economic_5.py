# Positive
# content of test_merge_4.py

import json
from pytest_bdd import scenario, given, then, when
from tests.models.indicator import Indicator
from tests.models.pause import Pause


with open("combo_merge.json") as file:
    json_data = json.loads(file.read())


@scenario('economic.feature', 'Getting ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins for combo-merge')
def test_coins_1():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause == True
    return {"game_progress": True}


@when("User merges multiple x houses of multiple n lvl", target_fixture="user_houses")
def merge_houses():
    houses = json_data.get('data')
    result = json_data.get('result')

    return houses, result


@then("User gets ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins")
def get_coins(user_houses):
    houses, result = user_houses
    indicator = Indicator()
    coins_result = indicator.combo_merged_houses(houses)
    assert coins_result == result
