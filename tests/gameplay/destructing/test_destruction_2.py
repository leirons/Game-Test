# content of test_destruction_2.py
# Negative test

from pytest_bdd import given, scenario, then, when


@scenario("destructing.feature", "Using the destruction function at empty cell")
def test_destruction_2():
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


@when("User try to destroy an empty cell", target_fixture="destroyed_house")
def destroyed_house(game_table):
    board = game_table

    assert board[0] == 0
    return False


@then("Nothing will happen")
def house(destroyed_house):
    assert destroyed_house is False


@then("From user wont take one possibility to destruction")
def check_ability(destruction_ability):
    ability = destruction_ability.get("destruction")
    assert ability == 1
