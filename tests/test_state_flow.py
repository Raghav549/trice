from trice.human.state_flow import StateFlow


def test_state_flow_snapshot_is_numeric():
    snapshot = StateFlow().snapshot()
    assert snapshot["alive"] == 1.0
    assert "attention" in snapshot
    assert all(isinstance(value, float) for value in snapshot.values())
