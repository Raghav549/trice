"""Finite-resource and energy allocation primitives."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EnergyBudget:
    """Track finite computational energy for an organism simulation."""

    capacity: float = 1.0
    level: float = 1.0
    basal_rate: float = 0.01

    def consume(self, amount: float) -> float:
        amount = max(0.0, amount)
        used = min(self.level, amount)
        self.level -= used
        return used

    def replenish(self, amount: float) -> float:
        amount = max(0.0, amount)
        gained = min(self.capacity - self.level, amount)
        self.level += gained
        return gained

    def step(self, dt: float = 1.0) -> float:
        return self.consume(self.basal_rate * max(0.0, dt))

    @property
    def fraction(self) -> float:
        if self.capacity <= 0:
            return 0.0
        return self.level / self.capacity
