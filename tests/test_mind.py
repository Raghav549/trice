from trice.human.mind import MindState


def test_mind_state_is_bounded():
    state = MindState(attention=2, valence=-2)
    state.clamp()
    assert state.attention == 1.0
    assert state.valence == -1.0
