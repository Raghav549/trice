from trice.physiology.endocrine_network import EndocrineNetwork
def test_endocrine_feedback():
    s=EndocrineNetwork().step(glucose=.8,stress=.3,energy=.7)
    assert s["insulin_signal"]>s["glucagon_signal"]
