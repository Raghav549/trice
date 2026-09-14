from trice.body import ComputationalBody


def test_integrated_body_steps_without_nan() -> None:
    body = ComputationalBody()
    state = body.step(0.1, {"vision": 0.5, "movement": 0.2, "food": 0.3, "stress": 0.1, "reward": 0.2})
    assert state
    assert all(isinstance(value, (int, float)) for value in state.values())
    assert all(value == value for value in state.values())


def test_body_dynamics_change_over_time() -> None:
    body = ComputationalBody()
    first = body.step(0.1, {"movement": 0.8, "stress": 0.7})
    second = body.step(0.1, {"movement": 0.0, "stress": 0.0, "sleep": 1.0})
    assert first != second
