# content of test_reward_6.py
# Negative test


from pytest_bdd import given, scenario, then, when


@scenario(
    "merge_reward.feature",
    "The user is trying to place the crystal that does not exists in queue",
)
def test_reward_6():
    pass


@given("A spawn queue without crystal", target_fixture="spawn_queue")
def spawn_queue():
    return [1, 2, 3, 4]


@given("Given Random numbers of houses on the game table", target_fixture="game_table")
def game_table():
    return [1, 2, 3, 4, 5, 6]


@given("Сrystal in the state of selecting an object to use", target_fixture="crystal")
def crystal():
    return "crystal"


@when(
    "User try to use the crystal on random house", target_fixture="try_to_use_crystal"
)
def try_to_use_crystal(game_table, spawn_queue, crystal):
    assert crystal not in spawn_queue
    result_board = game_table
    return [False, result_board]


@then("Nothing will happen")
def increase_lvl(crystal, try_to_use_crystal, game_table):
    is_used, board = try_to_use_crystal
    assert is_used is False
    assert board == game_table


@then("Nothing will happen")
def result(game_table):
    """Not implemented"""
    pass
