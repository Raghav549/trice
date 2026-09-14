"""Blood-cell and transport abstraction for the simulator."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BloodModel:
    red_cells: float = 1.0
    white_cells: float = 1.0
    platelets: float = 1.0
    hemoglobin: float = 1.0
    plasma_volume: float = 1.0
    clotting_signal: float = 0.0

    def step(self, dt: float, inflammation: float = 0.0, tissue_damage: float = 0.0, oxygen_demand: float = 0.2) -> dict[str, float]:
        dt = max(0.0, float(dt))
        inflammation = max(0.0, min(1.0, float(inflammation)))
        tissue_damage = max(0.0, min(1.0, float(tissue_damage)))
        oxygen_demand = max(0.0, min(1.0, float(oxygen_demand)))
        self.white_cells += (0.8 + 0.4 * inflammation - self.white_cells) * min(1.0, dt * 0.2)
        self.platelets += (1.0 - self.platelets) * min(1.0, dt * 0.1) - tissue_damage * 0.02 * dt
        self.clotting_signal += (tissue_damage - self.clotting_signal) * min(1.0, dt * 0.7)
        self.hemoglobin += ((1.0 - oxygen_demand * 0.2) - self.hemoglobin) * min(1.0, dt * 0.05)
        self.red_cells += (1.0 - self.red_cells) * min(1.0, dt * 0.02)
        self.plasma_volume += (1.0 - self.plasma_volume) * min(1.0, dt * 0.05)
        self.white_cells = max(0.0, self.white_cells)
        self.platelets = max(0.0, self.platelets)
        return {
            "red_cells": self.red_cells,
            "white_cells": self.white_cells,
            "platelets": self.platelets,
            "hemoglobin": self.hemoglobin,
            "plasma_volume": self.plasma_volume,
            "clotting_signal": self.clotting_signal,
        }
