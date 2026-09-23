from trice.human.respiration_state import RespirationState


def test_respiration_state_responds_to_demand():
    state = RespirationState()
    result = state.step(0.1, demand=0.5)
    assert result["respiratory_rate"] > 14
    assert result["oxygen_uptake"] > 0
