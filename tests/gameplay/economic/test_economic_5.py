# Positive
# content of test_merge_4.py
import json

from pytest_bdd import given, scenario, then, when, scenarios, parsers

from game.models.indicator import Indicator

# with open("combo_merge.json") as file:
#     json_data = json.loads(file.read())

# json_data = {
#     "//comment": "The data is  used for test_economic_5",
#     "data": [{"count": 3, "lvl": 1}, {"count": 4, "lvl": 2}],
#     "result": 22,
# }

EXTRA_TYPES = {
    "String": str
}

scenarios("combo_merge_outline_economic.feature")


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    return "board"


@given(
    parsers.cfparse("Gets {data:String} for combo-merging", extra_types=EXTRA_TYPES),
    target_fixture="coins",
)
def coins(data):
    indicator = Indicator()
    houses = json.loads(data)
    coins_result = indicator.combo_merged_houses(houses)
    return coins_result


@then(parsers.parse("User gets {result:d} coins"))
def coins_result(coins, result):
    assert result == coins
