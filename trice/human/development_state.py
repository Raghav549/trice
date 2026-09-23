"""Growth, development and aging state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DevelopmentState:
    age_years: float = 0.0
    growth: float = 0.0
    maturation: float = 0.0
    aging_load: float = 0.0
    repair_capacity: float = 1.0

    def step(self, dt_years: float) -> dict[str, float]:
        if dt_years < 0:
            raise ValueError("dt_years cannot be negative")
        self.age_years += float(dt_years)
        self.growth = max(0.0, min(1.0, 1.0 - max(0.0, self.age_years - 25.0) / 25.0))
        self.maturation = max(0.0, min(1.0, self.age_years / 25.0))
        self.aging_load = max(0.0, min(1.0, max(0.0, self.age_years - 30.0) / 70.0))
        self.repair_capacity = max(0.0, min(1.0, 1.0 - 0.6 * self.aging_load))
        return {
            "age_years": self.age_years,
            "growth": self.growth,
            "maturation": self.maturation,
            "aging_load": self.aging_load,
            "repair_capacity": self.repair_capacity,
        }
