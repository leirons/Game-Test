# content of test_destruction_7.py
# Negative test


from pytest_bdd import given, scenario, then, when


@scenario("destructing.feature", "Trying to destroy a house with 0 coins and no destruction function")
def test_destruction_7():
    pass


@given("Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    board = [1, 2, 3, 4, 5, 6]
    return board


@when("User tries to destroy a random house", target_fixture="destroyed_house")
def destroyed_house(game_table):
    for i in game_table:
        assert i != 0
    return False


@then("Nothing will happen")
def result(destroyed_house):
    assert destroyed_house is False
