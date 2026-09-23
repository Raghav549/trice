from trice.ai.neural_agent import NeuralAgent


def test_neural_agent_has_closed_loop_surface():
    agent = NeuralAgent()
    result = agent.step(0.1, {"vision": 0.5, "stress": 0.1})
    assert "movement" in result
    assert "attention" in result
