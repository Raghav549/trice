from trice.ai.action_selector import select_action


def test_select_action_normalizes_policy_output():
    action = select_action({"movement": 2.0, "attention": -1.0})
    assert action.movement == 1.0
    assert action.attention == 0.0
