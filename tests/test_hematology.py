from trice.physiology.hematology import HematologyModel

def test_blood_cells():
    s=HematologyModel().step(immune_signal=.8)
    assert s["rbc"]>0 and s["wbc"]>0
