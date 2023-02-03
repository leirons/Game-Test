# content of test_destruction_3.py
# Positive test

from pytest_bdd import given, scenario, then


@scenario(
    "destructing.feature", "Getting the destroy function  after receiving 200 coins"
)
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


@given("200 coins", target_fixture="coins")
def coins():
    return {"coins": 200}


@then("User gets one possibility to use the destruction function")
def get_destruction_ability(coins, destruction_ability):
    assert coins.get("coins") == 200
    ability = destruction_ability.get("destruction")
    assert ability == 1
    ability = ability + 1
    assert ability == 2
