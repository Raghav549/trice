"""Explicit internal physiological state vector."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class InternalState:
    blood_volume: float = 1.0
    glucose: float = 0.5
    oxygen: float = 1.0
    carbon_dioxide: float = 0.0
    body_energy: float = 1.0
    temperature: float = 1.0
    hydration: float = 1.0
    pain: float = 0.0

    def clamp(self) -> None:
        self.blood_volume = max(0.0, float(self.blood_volume))
        self.glucose = max(0.0, float(self.glucose))
        self.oxygen = max(0.0, float(self.oxygen))
        self.carbon_dioxide = max(0.0, float(self.carbon_dioxide))
        self.body_energy = max(0.0, min(1.0, float(self.body_energy)))
        self.temperature = max(0.0, min(2.0, float(self.temperature)))
        self.hydration = max(0.0, min(1.0, float(self.hydration)))
        self.pain = max(0.0, min(1.0, float(self.pain)))
