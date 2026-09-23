from trice.human.sensory_organs import SensoryOrgans


def test_sensory_organs_ingest_channels():
    senses = SensoryOrgans()
    result = senses.ingest({"vision": 2.0, "hearing": -2.0, "touch": 0.4})
    assert result["vision"] == 1.0
    assert result["hearing"] == -1.0
    assert result["touch"] == 0.4
