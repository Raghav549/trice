"""Higher-level organism cycle integrating the body simulator.

This layer deliberately contains orchestration only. Individual physiology
models remain independently testable and are still computational abstractions,
not validated human physiology.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from trice.body import ComputationalBody


@dataclass
class FullBodyCycle:
    """Run a complete body-inspired simulation step and retain the last state."""

    body: ComputationalBody = field(default_factory=ComputationalBody)
    time: float = 0.0
    last_state: dict[str, float] = field(default_factory=dict)

    def step(self, dt: float, inputs: Mapping[str, float] | None = None) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        normalized = {str(k): float(v) for k, v in (inputs or {}).items()}
        state = self.body.step(dt, normalized)
        self.time += dt
        self.last_state = dict(state)
        return dict(state)

    def run(self, steps: int, dt: float, inputs: Mapping[str, float] | None = None) -> list[dict[str, float]]:
        if steps < 0:
            raise ValueError("steps cannot be negative")
        return [self.step(dt, inputs) for _ in range(steps)]
