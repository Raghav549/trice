"""Canonical high-level homeostatic state vector."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HomeostaticState:
    energy: float = 1.0
    hydration: float = 1.0
    oxygenation: float = 1.0
    temperature: float = 1.0
    immune_load: float = 0.0
    stress: float = 0.0

    def clamp(self) -> None:
        for name in ("energy", "hydration", "oxygenation", "temperature"):
            value = getattr(self, name)
            setattr(self, name, max(0.0, min(1.0, float(value))))
        self.immune_load = max(0.0, min(1.0, float(self.immune_load)))
        self.stress = max(0.0, min(1.0, float(self.stress)))
