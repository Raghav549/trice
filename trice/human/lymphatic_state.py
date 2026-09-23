"""Lymphatic drainage and immune-transport state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LymphaticState:
    lymph_volume: float = 1.0
    drainage: float = 0.5
    node_activity: float = 0.5
    fluid_accumulation: float = 0.0

    def step(self, dt: float, inflammation: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        inflammation = max(0.0, min(1.0, float(inflammation)))
        self.node_activity = max(0.0, min(1.0, 0.5 + 0.5 * inflammation))
        self.drainage = max(0.0, min(1.0, 0.5 + 0.3 * self.node_activity))
        self.fluid_accumulation = max(
            0.0, min(1.0, self.fluid_accumulation + inflammation * dt * 0.1 - self.drainage * dt * 0.03)
        )
        self.lymph_volume = max(0.0, min(1.0, self.lymph_volume + self.drainage * dt * 0.01 - inflammation * dt * 0.005))
        return {
            "lymph_volume": self.lymph_volume,
            "lymph_drainage": self.drainage,
            "lymph_node_activity": self.node_activity,
            "fluid_accumulation": self.fluid_accumulation,
        }
