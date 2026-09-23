from trice.physiology.cardiac_cycle import CardiacCycle
def test_cardiac_output():
    s=CardiacCycle().step(demand=.8,sympathetic=.2)
    assert s["cardiac_output"]>0
