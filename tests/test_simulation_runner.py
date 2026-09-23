from trice.core.body_cycle import FullBodyCycle
from trice.core.simulation_runner import SimulationRunner


def test_runner_executes_fixed_steps():
    runner = SimulationRunner(FullBodyCycle(), 0.05, 4, {"movement": 0.2})
    states = runner.run()
    assert len(states) == 4
    assert runner.cycle.time == 0.2


def test_runner_rejects_invalid_dt():
    try:
        SimulationRunner(FullBodyCycle(), 0.0, 1).run()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
