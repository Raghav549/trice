"""Human lifecycle state machine."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LifecycleState:
    age_years: float = 0.0
    developmental_stage: str = "prenatal"
    alive: bool = True

    def step(self, dt_years: float) -> None:
        if dt_years < 0:
            raise ValueError("dt_years cannot be negative")
        if not self.alive:
            return
        self.age_years += float(dt_years)
        if self.age_years < 0.0:
            self.developmental_stage = "prenatal"
        elif self.age_years < 1.0:
            self.developmental_stage = "infancy"
        elif self.age_years < 12.0:
            self.developmental_stage = "childhood"
        elif self.age_years < 18.0:
            self.developmental_stage = "adolescence"
        elif self.age_years < 65.0:
            self.developmental_stage = "adult"
        else:
            self.developmental_stage = "older_adult"
