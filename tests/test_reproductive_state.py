from trice.human.reproductive_state import ReproductiveState


def test_reproductive_state_is_bounded():
    state = ReproductiveState(reproductive_maturity=2, cycle_phase=-1)
    state.clamp()
    assert state.reproductive_maturity == 1.0
    assert state.cycle_phase == 0.0
