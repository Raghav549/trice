from trice.human.whole_body_step import WholeBodyState


def test_whole_body_step_couples_major_systems():
    body = WholeBodyState()
    state = body.step(
        0.1,
        {
            "vision": 0.8,
            "movement": 0.5,
            "stress": 0.3,
            "water": 0.2,
            "ambient_temperature": 1.0,
        },
    )
    assert state["neural_arousal"] > 0.0
    assert state["oxygen_uptake"] > 0.0
    assert state["oxygen_delivery"] > 0.0
    assert state["renal_filtration"] > 0.0
    assert "core_temperature" in state
