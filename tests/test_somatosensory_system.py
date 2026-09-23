from trice.human.somatosensory_system import SomatosensorySystem


def test_somatosensory_system_tracks_modalities():
    result = SomatosensorySystem().ingest(touch=0.8, pressure=0.4, pain=0.7)
    assert result["touch_signal"] == 0.8
    assert result["pain_signal"] == 0.7
