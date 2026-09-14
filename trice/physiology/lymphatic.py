"""Lymphatic fluid return and immune-interface abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LymphaticModel:
    lymph_volume: float = 1.0
    drainage: float = 0.5
    immune_traffic: float = 0.5
    tissue_fluid: float = 1.0

    def step(self, dt: float, inflammation: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        inflammation = max(0.0, min(1.0, float(inflammation)))
        target_traffic = 0.4 + 0.5 * inflammation
        self.immune_traffic += (target_traffic - self.immune_traffic) * min(1.0, dt * 0.6)
        self.drainage += (0.5 + 0.3 * self.immune_traffic - self.drainage) * min(1.0, dt * 0.5)
        self.tissue_fluid += (1.0 + 0.3 * inflammation - self.tissue_fluid) * min(1.0, dt * 0.25)
        self.lymph_volume += (self.tissue_fluid * self.drainage - self.lymph_volume) * min(1.0, dt * 0.2)
        return {
            "lymph_volume": self.lymph_volume,
            "lymph_drainage": self.drainage,
            "immune_traffic": self.immune_traffic,
            "tissue_fluid": self.tissue_fluid,
        }
