from trice.core.full_body import FullBodyCycle


def test_full_body_cycle_runs_and_tracks_time():
    sim = FullBodyCycle()
    state = sim.step(0.1, {"food": 0.4, "water": 0.2, "movement": 0.3})
    assert sim.time == 0.1
    assert state
    assert sim.last_state == state


def test_full_body_run_returns_each_state():
    sim = FullBodyCycle()
    states = sim.run(3, 0.1, {"movement": 0.1})
    assert len(states) == 3
