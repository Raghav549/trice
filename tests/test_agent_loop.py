from trice.ai.loop import AgentLoop

def test_agent_loop_produces_action():
    action=AgentLoop().step({"energy":.8,"stress":.1})
    assert "movement" in action
    assert "attention" in action
