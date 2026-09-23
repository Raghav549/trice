from trice.human.metabolism_state import MetabolismState


def test_metabolism_state_responds_to_intake_and_activity():
    result = MetabolismState().step(1.0, intake=0.8, activity=0.5)
    assert result["metabolic_glucose"] > 0.5
    assert result["metabolic_demand"] > 0.2
