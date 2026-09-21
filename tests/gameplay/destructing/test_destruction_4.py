# content of test_destruction_4.py
# Positive test

from pytest_bdd import given, scenario, then, when


@scenario("destructing.feature", "Canceling the destroy function after clicking on it")
def test_destruction_4():
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


@when("User clicks on destroy button", target_fixture="destroy_process")
def destroy_process():
    return {"process": True}


@then(
    "There will be an option to cancel the destruction",
    target_fixture="cancel_destruction",
)
def cancel_destruction(destroy_process):
    process = destroy_process.get("process")
    assert process is True
    return {"process": True}


@when("User presses on the button to stop the destruction", target_fixture="user_press")
def user_press(cancel_destruction):
    process = False
    return {"process": process}


@then("The state of choosing a house to destroy disappears")
def changed_state(user_press):
    process = user_press.get("process")
    assert process is False
