from trice.human.endocrine_state import EndocrineState


def test_endocrine_state_clamps():
    state = EndocrineState(cortisol=2, melatonin=-1)
    state.clamp()
    assert state.cortisol == 1.0
    assert state.melatonin == 0.0
