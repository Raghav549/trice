"""Innate/adaptive immune state boundary."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ImmuneState:
    innate_activity: float = 0.5
    adaptive_activity: float = 0.5
    inflammation: float = 0.0
    pathogen_load: float = 0.0
    tissue_damage: float = 0.0

    def step(self, dt: float, pathogen_input: float = 0.0, damage_input: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.pathogen_load = max(0.0, min(1.0, self.pathogen_load + max(0.0, pathogen_input) * dt))
        self.tissue_damage = max(0.0, min(1.0, self.tissue_damage + max(0.0, damage_input) * dt))
        stimulus = max(self.pathogen_load, self.tissue_damage)
        self.innate_activity = max(0.0, min(1.0, 0.5 + 0.5 * stimulus))
        self.adaptive_activity = max(0.0, min(1.0, 0.5 + 0.4 * stimulus))
        self.inflammation = max(0.0, min(1.0, 0.7 * stimulus))
        return {
            "innate_activity": self.innate_activity,
            "adaptive_activity": self.adaptive_activity,
            "inflammation": self.inflammation,
            "pathogen_load": self.pathogen_load,
            "tissue_damage": self.tissue_damage,
        }
