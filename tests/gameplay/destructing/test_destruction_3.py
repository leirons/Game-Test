# content of test_destruction_3.py
# Positive test

from pytest_bdd import given, parsers, scenario, then


@scenario("destructing.feature", "Getting the destroy function  after receiving coins")
def test_destruction_3():
    pass


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [0, 0, 0, 0, 0, 0]
    return board


@given(
    "One possibility to use the destruction function",
    target_fixture="destruction_ability",
)
def destruction_ability():
    return {"destruction": 1}


@given(parsers.parse("User gets {coins:d} coins"), target_fixture="coins")
def coins(coins):
    return {"coins": coins}


@then("User gets possibility to use the destruction function")
def get_destruction_ability(coins, destruction_ability):
    coins = coins.get("coins")
    assert coins is not 0
    ability = destruction_ability.get("destruction")
    while coins >= 200:
        ability = ability + 1
        coins = coins - 200
    assert ability > 1
