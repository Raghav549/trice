from trice.human.action_loop import HumanActionLoop


def test_action_loop_produces_action_from_senses():
    loop = HumanActionLoop()
    action = loop.step({"vision": 1.0, "hearing": 0.2})
    assert "movement" in action
    assert "attention" in action
    assert 0.0 <= action["attention"] <= 1.0
