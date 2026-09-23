from trice.physiology.breathing import BreathingModel
def test_breathing_cycle():
    s=BreathingModel().step(oxygen_demand=.7,air_input=2)
    assert 0<=s["oxygenation"]<=1
    assert s["breath_cycle"]>=0
