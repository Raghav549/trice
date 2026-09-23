"""Material intake and first-pass processing abstractions.

This module turns environmental food/air/water inputs into typed internal
signals for downstream digestive, respiratory and fluid-balance models.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IntakeState:
    food: float = 0.0
    water: float = 0.0
    inhaled_air: float = 0.0
    oxygen_available: float = 0.21
    carbon_dioxide_exhaled: float = 0.0
    swallowed: float = 0.0


class IntakeModel:
    def step(self, *, food: float = 0.0, water: float = 0.0, air: float = 0.0, dt: float = 1.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        food = max(0.0, float(food))
        water = max(0.0, float(water))
        air = max(0.0, float(air))
        # Computational fractions, not human volumetric measurements.
        self.state.food += food * dt
        self.state.water += water * dt
        self.state.inhaled_air += air * dt
        self.state.swallowed = min(self.state.food, max(0.0, self.state.food * 0.98))
        return {
            "food_intake": self.state.food,
            "water_intake": self.state.water,
            "air_intake": self.state.inhaled_air,
            "swallowed": self.state.swallowed,
            "oxygen_available": self.state.oxygen_available,
        }

    def __init__(self) -> None:
        self.state = IntakeState()
