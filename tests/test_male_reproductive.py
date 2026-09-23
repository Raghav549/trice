from trice.human.male_reproductive import MaleReproductiveState


def test_male_reproductive_state_updates():
    result = MaleReproductiveState().step(3600.0, gonadal_drive=0.8)
    assert result["androgen_signal"] > 0.5
    assert 0.0 <= result["reproductive_capacity"] <= 1.0
