"""Production-oriented simulation runner with deterministic stepping."""
from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Callable

from .types import OrganismState
from .validation import HealthReport, bounded, finite


@dataclass(frozen=True)
class StepResult:
    """Result of one validated simulation step."""

    state: OrganismState
    wall_seconds: float
    report: HealthReport


class Simulation:
    """Run a TRICE organism with explicit step-size and safety limits."""

    def __init__(self, step_fn: Callable[[float], OrganismState], *, max_dt: float = 10.0) -> None:
        self._step_fn = step_fn
        self.max_dt = bounded(max_dt, "max_dt", 1e-9, 1e6)

    def step(self, dt: float = 1.0) -> StepResult:
        dt = bounded(dt, "dt", 1e-9, self.max_dt)
        start = perf_counter()
        state = self._step_fn(dt)
        elapsed = perf_counter() - start
        vector = state.vector()
        errors: list[str] = []
        try:
            for key, value in vector.items():
                finite(value, key)
        except ValueError as exc:
            errors.append(str(exc))
        report = HealthReport(
            finite=not errors,
            bounded_energy=0.0 <= state.energy <= 1.0,
            state_count=len(vector),
            errors=tuple(errors),
        )
        return StepResult(state=state, wall_seconds=elapsed, report=report)

    def run(self, steps: int, dt: float = 1.0) -> list[StepResult]:
        if steps < 0:
            raise ValueError("steps must be >= 0")
        return [self.step(dt) for _ in range(steps)]
