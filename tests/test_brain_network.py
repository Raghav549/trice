from trice.human.brain_network import BrainNetwork


def test_brain_network_couples_sensory_reward_and_threat():
    result = BrainNetwork().step(
        0.1,
        sensory_input=0.8,
        reward=0.5,
        threat=0.7,
        motor_feedback=0.4,
    )
    assert result["thalamus_state"] > 0.5
    assert result["hypothalamus_state"] > 0.5
    assert result["hippocampus_state"] > 0.5
