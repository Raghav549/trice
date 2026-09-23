from trice.human.internal_state import InternalState


def test_internal_state_clamps_nonnegative_resources():
    state = InternalState(glucose=-1, oxygen=-1, hydration=2, pain=-3)
    state.clamp()
    assert state.glucose == 0
    assert state.oxygen == 0
    assert state.hydration == 1
    assert state.pain == 0
