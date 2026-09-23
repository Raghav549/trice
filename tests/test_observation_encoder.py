from trice.ai.observation_encoder import encode


def test_encoder_has_stable_width():
    vector = encode({"body_energy": 0.8, "stress": 0.2})
    assert len(vector) == 9
    assert vector[0] == 0.8
