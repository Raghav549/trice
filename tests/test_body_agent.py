from trice.ai.body_agent import BodyAgent


def test_body_agent_closes_policy_body_loop():
    agent = BodyAgent()
    action = agent.step(0.1, {"reward": 0.2, "stress": 0.1})
    assert "movement" in action
    assert "attention" in action
    assert agent.body.cognition is not None
