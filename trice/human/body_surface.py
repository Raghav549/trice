"""External body surface state."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BodySurface:
    skin_integrity: float = 1.0
    hydration: float = 1.0
    barrier_function: float = 1.0
    wound_load: float = 0.0
    hair_coverage: float = 1.0
    nail_integrity: float = 1.0

    def step(self, dt: float, injury: float = 0.0, dryness: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.wound_load = max(0.0, min(1.0, self.wound_load + float(injury) * dt))
        self.wound_load = max(0.0, self.wound_load - 0.05 * dt)
        self.hydration = max(0.0, min(1.0, self.hydration - max(0.0, dryness) * dt))
        self.barrier_function = max(0.0, min(1.0, self.skin_integrity * self.hydration))
        return {
            "skin_integrity": self.skin_integrity,
            "skin_hydration": self.hydration,
            "barrier_function": self.barrier_function,
            "wound_load": self.wound_load,
            "hair_coverage": self.hair_coverage,
            "nail_integrity": self.nail_integrity,
        }
