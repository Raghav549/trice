from trice.human.digestive_state import DigestiveState


def test_digestive_state_moves_and_absorbs_food():
    state = DigestiveState()
    result = state.step(1.0, food=1.0)
    assert result["stomach_content"] < 1.0
    assert result["absorbed_glucose"] > 0
