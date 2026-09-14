import pytest

from trice.organism import TriceOrganism
from trice.research import run_benchmark


def test_benchmark_is_deterministic_for_fresh_organisms() -> None:
    first = run_benchmark("smoke", TriceOrganism, steps=8, dt=0.25)
    second = run_benchmark("smoke", TriceOrganism, steps=8, dt=0.25)
    assert first.digest == second.digest
    assert first.steps == 8
    assert first.metrics["finite"] is True


@pytest.mark.parametrize("steps", [-1, -10])
def test_benchmark_rejects_negative_steps(steps: int) -> None:
    with pytest.raises(ValueError, match="steps"):
        run_benchmark("invalid", TriceOrganism, steps=steps)


@pytest.mark.parametrize("dt", [0.0, -1.0, float("nan"), float("inf")])
def test_benchmark_rejects_invalid_dt(dt: float) -> None:
    with pytest.raises(ValueError, match="dt"):
        run_benchmark("invalid", TriceOrganism, steps=1, dt=dt)


def test_benchmark_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="name"):
        run_benchmark("   ", TriceOrganism, steps=1)
