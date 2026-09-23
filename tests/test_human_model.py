from trice.human.human_model import HumanModel


def test_human_model_runs_integrated_cycle():
    model = HumanModel()
    state = model.step(0.1, {"movement": 0.2, "food": 0.3, "stress": 0.1})
    assert state["time"] == 0.1
    assert "body_energy" in state
    assert "attention" in state
