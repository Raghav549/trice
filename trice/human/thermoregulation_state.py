"""Core thermoregulation state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ThermoregulationState:
    core_temperature: float = 1.0
    heat_production: float = 0.5
    heat_loss: float = 0.5
    sweating: float = 0.0
    shivering: float = 0.0

    def step(self, dt: float, ambient_temperature: float = 1.0, activity: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        ambient = float(ambient_temperature)
        activity = max(0.0, min(1.0, float(activity)))
        error = self.core_temperature - ambient
        self.sweating = max(0.0, min(1.0, error * 4.0))
        self.shivering = max(0.0, min(1.0, -error * 4.0))
        self.heat_production = 0.5 + 0.3 * activity + 0.3 * self.shivering
        self.heat_loss = max(0.0, 0.5 + 0.5 * self.sweating)
        self.core_temperature += 0.02 * (self.heat_production - self.heat_loss) * dt
        return {
            "core_temperature": self.core_temperature,
            "heat_production": self.heat_production,
            "heat_loss": self.heat_loss,
            "sweating": self.sweating,
            "shivering": self.shivering,
        }
