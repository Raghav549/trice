from trice.human.homeostatic_state import HomeostaticState


def test_homeostatic_state_clamps():
    state = HomeostaticState(energy=2, hydration=-1, oxygenation=1.5, stress=-0.5)
    state.clamp()
    assert state.energy == 1.0
    assert state.hydration == 0.0
    assert state.oxygenation == 1.0
    assert state.stress == 0.0
