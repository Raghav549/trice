from trice.human.lymphatic_state import LymphaticState


def test_lymphatic_state_responds_to_inflammation():
    state = LymphaticState()
    result = state.step(1.0, inflammation=0.8)
    assert result["lymph_node_activity"] > 0.5
    assert result["lymph_volume"] >= 0.0
