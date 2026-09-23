"""Small deterministic runner for repeatable TRICE experiments."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .body_cycle import FullBodyCycle


@dataclass
class SimulationRunner:
    """Run a body cycle for a fixed number of steps."""

    cycle: FullBodyCycle
    dt: float
    steps: int
    inputs: Mapping[str, float] | None = None

    def run(self) -> list[dict[str, float]]:
        if self.dt <= 0:
            raise ValueError("dt must be positive")
        if self.steps < 0:
            raise ValueError("steps cannot be negative")
        return self.cycle.run(self.steps, self.dt, self.inputs)
