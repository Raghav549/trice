"""Computational balance and vestibular state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VestibularSystem:
    acceleration: float = 0.0
    rotation: float = 0.0
    balance_confidence: float = 1.0
    nausea_signal: float = 0.0

    def ingest(self, acceleration: float = 0.0, rotation: float = 0.0) -> dict[str, float]:
        self.acceleration = float(acceleration)
        self.rotation = float(rotation)
        mismatch = min(1.0, abs(self.acceleration - self.rotation))
        self.balance_confidence = max(0.0, 1.0 - 0.6 * mismatch)
        self.nausea_signal = max(0.0, min(1.0, 0.8 * mismatch))
        return {
            "vestibular_acceleration": self.acceleration,
            "vestibular_rotation": self.rotation,
            "balance_confidence": self.balance_confidence,
            "nausea_signal": self.nausea_signal,
        }
