from trice.human.brain_state import BrainState


def test_brain_state_integrates_sensory_reward_and_threat():
    result = BrainState().step(0.1, sensory_salience=0.8, reward=0.5, threat=0.6)
    assert result["brain_attention"] > 0.5
    assert result["brain_threat_response"] > 0.0
    assert result["executive_control"] >= 0.0
