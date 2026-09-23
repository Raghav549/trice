from trice.human.integument_state import IntegumentState


def test_integument_state_updates():
    state = IntegumentState()
    result = state.step(1.0, heat=0.8, injury=0.1)
    assert result["hair_growth"] > 1.0
    assert result["nail_growth"] > 1.0
    assert 0.0 <= result["skin_integrity"] <= 1.0
