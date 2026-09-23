from trice.human.vision_system import VisionSystem


def test_vision_system_extracts_visual_salience():
    result = VisionSystem().ingest(luminance=0.6, contrast=0.8, motion=0.4)
    assert result["visual_salience"] == 0.6
    assert result["visual_luminance"] == 0.6
