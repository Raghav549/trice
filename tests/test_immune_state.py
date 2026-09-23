from trice.human.immune_state import ImmuneState


def test_immune_state_responds_to_pathogen():
    state = ImmuneState()
    result = state.step(0.1, pathogen_input=0.8)
    assert result["innate_activity"] > 0.5
    assert result["inflammation"] > 0
