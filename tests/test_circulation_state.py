from trice.human.circulation_state import CirculationState


def test_circulation_state_responds_to_activity():
    state = CirculationState()
    result = state.step(0.1, activity=0.8)
    assert result["cardiac_output"] > 1.0
    assert result["oxygen_delivery"] > 0.0
