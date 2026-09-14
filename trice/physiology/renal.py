"""Renal water/electrolyte homeostasis abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RenalModel:
    total_water: float = 1.0
    sodium: float = 1.0
    potassium: float = 1.0
    acid_base: float = 1.0
    filtration: float = 1.0

    def step(self, dt: float, intake: float = 0.0, metabolic_load: float = 0.2) -> dict[str, float]:
        dt = max(0.0, float(dt))
        intake = max(0.0, float(intake))
        load = max(0.0, min(1.0, float(metabolic_load)))
        self.filtration += (1.0 + 0.3 * load - self.filtration) * min(1.0, dt * 0.5)
        excretion = 0.01 * self.filtration * dt
        self.total_water += intake * dt - excretion
        self.total_water += (1.0 - self.total_water) * min(1.0, dt * 0.15)
        self.sodium += (1.0 - self.sodium) * min(1.0, dt * 0.1)
        self.potassium += (1.0 - self.potassium) * min(1.0, dt * 0.12)
        self.acid_base += (1.0 - self.acid_base) * min(1.0, dt * 0.18) - 0.01 * load * dt
        self.acid_base = max(0.0, min(2.0, self.acid_base))
        return {
            "renal_water": self.total_water,
            "renal_sodium": self.sodium,
            "renal_potassium": self.potassium,
            "renal_acid_base": self.acid_base,
            "renal_filtration": self.filtration,
        }
