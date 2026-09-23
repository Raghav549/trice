"""Energy and substrate metabolism state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MetabolismState:
    glucose: float = 0.5
    glycogen: float = 0.5
    fat_store: float = 0.5
    body_energy: float = 0.8
    metabolic_demand: float = 0.2

    def step(self, dt: float, intake: float = 0.0, activity: float = 0.0, stress: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        intake = max(0.0, float(intake))
        activity = max(0.0, min(1.0, float(activity)))
        stress = max(0.0, min(1.0, float(stress)))
        self.metabolic_demand = max(0.0, min(1.0, 0.2 + 0.5 * activity + 0.2 * stress))
        self.glucose = max(0.0, min(1.0, self.glucose + 0.2 * intake * dt - 0.1 * self.metabolic_demand * dt))
        self.glycogen = max(0.0, min(1.0, self.glycogen + 0.05 * intake * dt - 0.05 * activity * dt))
        self.fat_store = max(0.0, min(1.0, self.fat_store + 0.02 * intake * dt - 0.02 * activity * dt))
        self.body_energy = max(0.0, min(1.0, self.body_energy + 0.08 * intake * dt - 0.1 * self.metabolic_demand * dt))
        return {
            "metabolic_glucose": self.glucose,
            "metabolic_glycogen": self.glycogen,
            "metabolic_fat_store": self.fat_store,
            "metabolic_body_energy": self.body_energy,
            "metabolic_demand": self.metabolic_demand,
        }
