from trice.physiology.oral import OralModel
def test_oral_processing():
    s=OralModel().step(food=3,chewing=.8,taste=.3,saliva=.7,swallow=True)
    assert s["swallow_signal"]==1.0
