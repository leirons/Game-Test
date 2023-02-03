# content of test_reward_5.py
# Negative test


from pytest_bdd import given, scenario, then, when

@scenario("merge_reward.feature", "Try to use crystal at spawn place")
def test_reward_5():
    pass


@given("A crystal after combo-merge case", target_fixture="crystal")
def crystal():
    return {"crystal": True}


@when(
    "User drags the crystal to any house at spawn place", target_fixture="drag_crystal"
)
def drag_crystal():
    return {"crystal_is_dragged": True}


@then("Nothing will happen")
def increase_lvl(crystal, drag_crystal):
    increased = False

    is_dragged = drag_crystal.get("crystal_is_dragged")
    crystal = crystal.get("crystal")

    assert is_dragged is True
    assert crystal is True
    assert increased is False
