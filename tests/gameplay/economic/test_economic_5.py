# Positive
# content of test_merge_4.py

from pytest_bdd import given, scenario, then, when

from game.models.indicator import Indicator
from game.models.pause import Pause

# with open("combo_merge.json") as file:
#     json_data = json.loads(file.read())
json_data = {
    "//comment": "The data is  used for test_economic_5",
    "data": [{"count": 3, "lvl": 1}, {"count": 4, "lvl": 2}],
    "result": 22,
}


@scenario(
    "economic.feature",
    "Getting ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins for combo-merge",
)
def test_coins_5():
    pass


@given("The game is in progress", target_fixture="game_in_progress")
def game_in_progress():
    pause = Pause()
    assert pause.active_pause
    return {"game_progress": True}


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    return "board"


@when("User merges multiple x houses of multiple n lvl", target_fixture="user_houses")
def merge_houses(game_table):
    # TODO: move this one into examples for x and n
    # https://pytest-bdd.readthedocs.io/en/stable/#scenario-outlines
    houses = json_data.get("data")
    result = json_data.get("result")

    return houses, result


@then("User gets ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins")
def get_coins(user_houses):
    houses, result = user_houses
    indicator = Indicator()
    coins_result = indicator.combo_merged_houses(houses)
    assert coins_result == result


@when("User presses on the button to stop the destruction")
def step_impl():
    raise NotImplementedError(
        "STEP: When User presses on the button to stop the destruction"
    )
