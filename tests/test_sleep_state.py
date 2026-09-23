from trice.human.sleep_state import SleepState


def test_sleep_state_tracks_sleep_pressure_and_awake():
    state = SleepState()
    result = state.step(1.0)
    assert result["sleep_pressure"] > 0
    assert result["awake"] == 1.0


def test_sleep_input_changes_awake_state():
    state = SleepState()
    assert state.step(1.0, sleep_input=1.0)["awake"] == 0.0
