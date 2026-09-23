"""Blood-cell and plasma state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HematologyState:
    red_cells: float = 1.0
    white_cells: float = 1.0
    platelets: float = 1.0
    plasma_volume: float = 1.0
    hemoglobin_capacity: float = 1.0

    def clamp(self) -> None:
        for name in ("red_cells", "white_cells", "platelets", "plasma_volume", "hemoglobin_capacity"):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))

    def oxygen_capacity(self) -> float:
        return max(0.0, min(1.0, self.red_cells * self.hemoglobin_capacity))
