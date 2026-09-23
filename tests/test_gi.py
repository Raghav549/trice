from trice.physiology.gi import GIModel

def test_gi_flow():
    s=GIModel().step(food=4,water=2)
    assert s["oral"]>=0
