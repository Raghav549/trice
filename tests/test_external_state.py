from trice.human.external_state import ExternalState


def test_external_state_movement():
    state = ExternalState()
    state.move(1, -2, 0.5)
    assert state.position == (1.0, -2.0, 0.5)
