"""Low-order cardiovascular flow model.

This is an engineering approximation for simulation, not a clinical model.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CardiovascularModel:
    heart_rate: float = 70.0
    stroke_volume: float = 70.0
    vascular_resistance: float = 1.0
    arterial_pressure: float = 1.0
    venous_return: float = 1.0

    def step(self, dt: float, activity: float = 0.0) -> dict[str, float]:
        demand = max(0.0, min(1.0, float(activity)))
        target_hr = 65.0 + 55.0 * demand
        self.heart_rate += (target_hr - self.heart_rate) * min(1.0, dt * 0.5)
        self.stroke_volume = 70.0 * (1.0 - 0.15 * demand)
        cardiac_output = self.heart_rate * self.stroke_volume / 1000.0
        target_pressure = cardiac_output / max(self.vascular_resistance, 1e-6)
        self.arterial_pressure += (target_pressure - self.arterial_pressure) * min(1.0, dt * 0.8)
        self.venous_return += (self.arterial_pressure - self.venous_return) * min(1.0, dt * 0.6)
        return {
            "heart_rate": self.heart_rate,
            "stroke_volume": self.stroke_volume,
            "cardiac_output": cardiac_output,
            "arterial_pressure": self.arterial_pressure,
            "venous_return": self.venous_return,
        }
