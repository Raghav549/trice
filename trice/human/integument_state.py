"""Skin, hair and nail growth state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IntegumentState:
    skin_integrity: float = 1.0
    hair_growth: float = 1.0
    nail_growth: float = 1.0
    sebum: float = 0.5
    sweat: float = 0.0
    wound_load: float = 0.0

    def step(self, dt: float, heat: float = 0.0, injury: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        heat = max(0.0, min(1.0, float(heat)))
        injury = max(0.0, min(1.0, float(injury)))
        self.wound_load = max(0.0, min(1.0, self.wound_load + injury * dt - 0.05 * dt))
        self.skin_integrity = max(0.0, min(1.0, self.skin_integrity - injury * dt * 0.05))
        self.sweat = max(0.0, min(1.0, 0.8 * self.sweat + 0.2 * heat))
        self.sebum = max(0.0, min(1.0, 0.98 * self.sebum + 0.02 * (1.0 - heat)))
        self.hair_growth = max(0.0, self.hair_growth + 0.001 * dt)
        self.nail_growth = max(0.0, self.nail_growth + 0.002 * dt)
        return {
            "skin_integrity": self.skin_integrity,
            "hair_growth": self.hair_growth,
            "nail_growth": self.nail_growth,
            "sebum": self.sebum,
            "sweat": self.sweat,
            "wound_load": self.wound_load,
        }
