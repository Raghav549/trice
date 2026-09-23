from trice.physiology.sleep_cycle import SleepCycle
def test_sleep_wake():
    s=SleepCycle().step(sleeping=True,light=.1)
    assert s["sleep_depth"]>0
