"""Generic reproductive-cycle state progression."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReproductiveCycle:
    phase: float = 0.0
    period: float = 28.0
    active: bool = True

    def step(self, dt_days: float) -> float:
        if dt_days < 0:
            raise ValueError("dt_days cannot be negative")
        if self.period <= 0:
            raise ValueError("period must be positive")
        if not self.active:
            return self.phase
        self.phase = (self.phase + float(dt_days) / self.period) % 1.0
        return self.phase
