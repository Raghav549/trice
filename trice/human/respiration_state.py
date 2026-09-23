"""High-level ventilation and gas-exchange state."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RespirationState:
    respiratory_rate: float = 14.0
    ventilation: float = 1.0
    oxygen_uptake: float = 1.0
    carbon_dioxide_output: float = 1.0

    def step(self, dt: float, demand: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        demand = max(0.0, min(1.0, float(demand)))
        self.respiratory_rate = max(0.0, 14.0 + 8.0 * demand)
        self.ventilation = max(0.0, 1.0 + demand)
        self.oxygen_uptake = max(0.0, self.ventilation * 0.9)
        self.carbon_dioxide_output = max(0.0, self.ventilation * 0.8)
        return {
            "respiratory_rate": self.respiratory_rate,
            "ventilation": self.ventilation,
            "oxygen_uptake": self.oxygen_uptake,
            "carbon_dioxide_output": self.carbon_dioxide_output,
        }
