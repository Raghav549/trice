"""Fluid and electrolyte balance state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FluidBalance:
    water: float = 1.0
    sodium: float = 1.0
    potassium: float = 1.0

    def step(self, dt: float, water_intake: float = 0.0, loss: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.water = max(0.0, min(1.0, self.water + float(water_intake) * dt - max(0.0, float(loss)) * dt))
        self.sodium = max(0.0, min(1.0, self.sodium + 0.02 * water_intake * dt - 0.01 * loss * dt))
        self.potassium = max(0.0, min(1.0, self.potassium + 0.01 * water_intake * dt - 0.008 * loss * dt))
        return {"water": self.water, "sodium": self.sodium, "potassium": self.potassium}
