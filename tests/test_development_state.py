from trice.human.development_state import DevelopmentState


def test_development_state_progresses():
    state = DevelopmentState()
    result = state.step(20.0)
    assert result["maturation"] > 0
    assert result["aging_load"] == 0.0
