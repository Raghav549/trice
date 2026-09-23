from trice.human.gustatory_system import GustatorySystem


def test_gustatory_system_tracks_taste_channels():
    result = GustatorySystem().ingest({"sweet": 0.9, "bitter": 0.3})
    assert result["taste_sweet"] == 0.9
    assert result["taste_bitter"] == 0.3
