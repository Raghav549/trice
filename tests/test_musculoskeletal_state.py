from trice.human.musculoskeletal_state import MusculoskeletalState


def test_musculoskeletal_state_updates():
    state = MusculoskeletalState()
    result = state.step(0.1, command=0.8, load=0.2)
    assert result["muscle_activation"] > 0
    assert 0.0 <= result["balance"] <= 1.0
