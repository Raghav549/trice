from trice.human.whole_human import WholeHuman


def test_whole_human_runs_integrated_layers():
    human = WholeHuman()
    state = human.step(0.1, {"movement": 0.2, "stress": 0.1, "water": 0.1})
    assert "time" in state
    assert "neural_arousal" in state
    assert "heart_rate" not in state  # this layer remains explicitly separated from the high-level abstraction
