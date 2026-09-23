from trice.human.body_state import HumanState


def test_human_state_validates_and_clamps():
    state = HumanState()
    state.internal.glucose = -1
    state.homeostasis.energy = 3
    state.validate()
    assert state.internal.glucose == 0
    assert state.homeostasis.energy == 1
