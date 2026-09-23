from trice.physiology.musculoskeletal import MusculoskeletalModel
def test_force_generation():
    s=MusculoskeletalModel().step(command=.9,conditioning=.8)
    assert s["force"]>0
