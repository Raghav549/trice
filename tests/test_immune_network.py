from trice.physiology.immune_network import ImmuneNetwork
def test_immune_response():
    s=ImmuneNetwork().step(antigen=.8,damage=.2)
    assert 0<=s["inflammation"]<=1
