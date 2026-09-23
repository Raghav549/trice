from trice.human.autonomic_state import AutonomicState


def test_autonomic_state_responds_to_stress():
    result = AutonomicState().step(0.1, stress=0.9)
    assert result["sympathetic_tone"] > 0.5
    assert result["autonomic_arousal"] > 0.5
