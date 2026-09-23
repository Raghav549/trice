from trice.human.nervous_state import NervousState


def test_nervous_state_responds_to_threat():
    state = NervousState()
    result = state.step(0.1, sensory_load=0.4, threat=0.9)
    assert result["neural_arousal"] > 0.5
    assert result["reflex_readiness"] > 0.5
