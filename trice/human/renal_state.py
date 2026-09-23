"""Kidney filtration and urinary state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RenalState:
    filtration: float = 1.0
    water_balance: float = 1.0
    sodium_balance: float = 1.0
    urine_volume: float = 0.0

    def step(self, dt: float, hydration: float = 1.0, solute_load: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        hydration = max(0.0, min(1.0, float(hydration)))
        solute_load = max(0.0, min(1.0, float(solute_load)))
        self.filtration = max(0.0, min(1.0, 0.5 + 0.5 * hydration - 0.2 * solute_load))
        urine_rate = max(0.0, 0.08 * self.filtration * (1.0 - 0.5 * hydration) + 0.02 * solute_load)
        self.urine_volume = max(0.0, self.urine_volume + urine_rate * dt)
        self.water_balance = max(0.0, min(1.0, hydration - urine_rate * dt))
        self.sodium_balance = max(0.0, min(1.0, 1.0 - 0.25 * solute_load))
        return {
            "renal_filtration": self.filtration,
            "water_balance": self.water_balance,
            "sodium_balance": self.sodium_balance,
            "urine_volume": self.urine_volume,
        }
