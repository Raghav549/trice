"""Integrated blood and circulation state boundary."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CirculationState:
    blood_volume: float = 1.0
    cardiac_output: float = 1.0
    vascular_tone: float = 0.5
    oxygen_delivery: float = 1.0

    def step(self, dt: float, activity: float = 0.0, blood_loss: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        activity = max(0.0, min(1.0, float(activity)))
        self.blood_volume = max(0.0, self.blood_volume - max(0.0, blood_loss) * dt)
        self.cardiac_output = max(0.0, 1.0 + 0.5 * activity)
        self.vascular_tone = max(0.0, min(1.0, 0.5 + 0.2 * activity))
        self.oxygen_delivery = max(0.0, self.blood_volume * self.cardiac_output)
        return {
            "blood_volume": self.blood_volume,
            "cardiac_output": self.cardiac_output,
            "vascular_tone": self.vascular_tone,
            "oxygen_delivery": self.oxygen_delivery,
        }
