"""Whole-body energy and nutrient-flow abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MetabolismModel:
    glucose: float = 1.0
    glycogen: float = 1.0
    fat: float = 1.0
    protein_pool: float = 1.0
    metabolic_rate: float = 1.0
    body_energy: float = 1.0

    def step(self, dt: float, intake: float = 0.0, activity: float = 0.0, stress: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        intake = max(0.0, float(intake))
        activity = max(0.0, min(1.0, float(activity)))
        stress = max(0.0, min(1.0, float(stress)))
        demand = (0.08 + 0.20 * activity + 0.05 * stress) * self.metabolic_rate
        self.glucose += intake * 0.15 * dt - demand * dt
        if self.glucose < 0.25:
            mobilize = min(self.glycogen, 0.12 * dt)
            self.glycogen -= mobilize
            self.glucose += mobilize
        if self.glucose < 0.15:
            mobilize_fat = min(self.fat, 0.05 * dt)
            self.fat -= mobilize_fat
            self.glucose += 0.5 * mobilize_fat
        self.glucose = max(0.0, min(2.0, self.glucose))
        self.glycogen = max(0.0, self.glycogen)
        self.fat = max(0.0, self.fat)
        self.body_energy += (self.glucose + 0.5 * self.fat - self.body_energy) * min(1.0, dt * 0.05)
        return {
            "glucose": self.glucose,
            "glycogen": self.glycogen,
            "fat": self.fat,
            "protein_pool": self.protein_pool,
            "metabolic_rate": self.metabolic_rate,
            "body_energy": self.body_energy,
        }
