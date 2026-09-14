"""Low-order respiratory gas-exchange model."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RespiratoryModel:
    ventilation: float = 1.0
    oxygen: float = 0.21
    carbon_dioxide: float = 0.04
    respiratory_drive: float = 0.0

    def step(self, dt: float, metabolic_demand: float = 0.2) -> dict[str, float]:
        dt = max(0.0, float(dt))
        demand = max(0.0, min(1.0, float(metabolic_demand)))
        target_drive = demand * 2.0 + max(0.0, self.carbon_dioxide - 0.04) * 4.0
        self.respiratory_drive += (target_drive - self.respiratory_drive) * min(1.0, dt * 0.8)
        self.ventilation += (1.0 + self.respiratory_drive - self.ventilation) * min(1.0, dt * 0.7)
        extraction = min(0.15, 0.03 + 0.08 * demand)
        self.oxygen += ((0.21 - self.oxygen) * 0.2 - extraction * self.ventilation) * dt
        self.carbon_dioxide += (0.04 - self.carbon_dioxide) * 0.4 * dt + 0.02 * demand * dt
        self.oxygen = max(0.0, min(1.0, self.oxygen))
        self.carbon_dioxide = max(0.0, min(1.0, self.carbon_dioxide))
        return {
            "ventilation": self.ventilation,
            "oxygen": self.oxygen,
            "carbon_dioxide": self.carbon_dioxide,
            "respiratory_drive": self.respiratory_drive,
        }
