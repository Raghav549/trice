from trice.core.observations import observe


def test_observe_has_stable_schema():
    result = observe({"body_energy": 0.8, "stress": 0.1})
    assert result["body_energy"] == 0.8
    assert result["stress"] == 0.1
    assert "heart_rate" in result
    assert set(result) == {
        "body_energy", "glucose", "heart_rate", "oxygen",
        "temperature", "stress", "attention", "pain", "arousal",
    }
