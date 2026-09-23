from trice.physiology.integument import IntegumentModel

def test_skin_hair_nail_state():
    s=IntegumentModel().step(temperature=.8,stress=.2,hydration=.7)
    assert 0<=s["barrier"]<=1
    assert s["hair_growth"]>=0
