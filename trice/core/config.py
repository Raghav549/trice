"""Explicit simulator configuration with validation and reproducibility."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfig:
    """Runtime configuration shared by production simulations."""

    seed: int = 0
    dt: float = 0.1
    max_steps: int = 10000
    fail_on_nonfinite: bool = True

    def validate(self) -> None:
        if self.dt <= 0.0:
            raise ValueError("dt must be > 0")
        if self.max_steps < 0:
            raise ValueError("max_steps must be >= 0")
        if self.seed < 0:
            raise ValueError("seed must be >= 0")
