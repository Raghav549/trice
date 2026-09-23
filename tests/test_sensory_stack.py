from trice.human.sensory_stack import CHANNELS, normalize_senses


def test_sensory_stack_has_explicit_channels():
    senses = normalize_senses({"vision": 2.0, "pain": -2.0})
    assert senses["vision"] == 1.0
    assert senses["pain"] == -1.0
    assert set(senses) == set(CHANNELS)
