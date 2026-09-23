from trice.human.behavior import BehavioralState


def test_behavioral_drives_are_bounded():
    state = BehavioralState(hunger=2, thirst=-1)
    state.clamp()
    assert state.hunger == 1.0
    assert state.thirst == 0.0
