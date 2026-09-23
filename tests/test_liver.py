from trice.physiology.liver import LiverModel

def test_liver_processing():
    s=LiverModel().step(glucose=.8,amino_acids=.7,fats=.6,toxin_input=.2)
    assert s["glycogen"]>0
