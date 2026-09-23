"""Upper airway, swallowing and oral processing state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OralAirwayState:
    salivary_flow: float = 0.5
    swallow_ready: float = 1.0
    airway_patency: float = 1.0
    oral_load: float = 0.0

    def step(self, dt: float, food: float = 0.0, obstruction: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        food = max(0.0, min(1.0, float(food)))
        obstruction = max(0.0, min(1.0, float(obstruction)))
        self.salivary_flow = max(0.0, min(1.0, 0.8 * self.salivary_flow + 0.2 * food))
        self.swallow_ready = max(0.0, min(1.0, 0.9 * self.swallow_ready + 0.1 * (1.0 - obstruction)))
        self.airway_patency = max(0.0, min(1.0, 1.0 - obstruction))
        self.oral_load = max(0.0, min(1.0, self.oral_load + food * dt - 0.1 * dt))
        return {
            "salivary_flow": self.salivary_flow,
            "swallow_ready": self.swallow_ready,
            "airway_patency": self.airway_patency,
            "oral_load": self.oral_load,
        }
