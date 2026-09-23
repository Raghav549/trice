from trice.human.female_reproductive import FemaleReproductiveState


def test_female_reproductive_state_progresses():
    result = FemaleReproductiveState().step(86400.0, gonadal_drive=0.7)
    assert 0.0 <= result["estrogen_signal"] <= 1.0
    assert result["reproductive_cycle_phase"] > 0.0
