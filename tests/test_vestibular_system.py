from trice.human.vestibular_system import VestibularSystem


def test_vestibular_system_tracks_balance_confidence():
    result = VestibularSystem().ingest(acceleration=0.8, rotation=0.1)
    assert result["balance_confidence"] < 1.0
    assert result["nausea_signal"] > 0
