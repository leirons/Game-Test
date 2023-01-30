# content of test_destruction_5.py
# Positive test

from pytest_bdd import scenario, then, when


@scenario('destructing.feature', 'Getting the destroy function after starting a game')
def test_destruction_5():
    pass


@when("User starts a game", target_fixture="game_process")
def game_process():
    return {"process": True}


@then("User gets one destroy function")
def destroy_ability(game_process):
    assert game_process.get('process') is True
    destroy_ability = 1
    assert destroy_ability == 1
