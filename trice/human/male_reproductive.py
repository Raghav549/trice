"""Detailed male reproductive state surface.

This is a simulation abstraction, not a clinical or fertility predictor.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MaleReproductiveState:
    gonadal_activity: float = 0.5
    androgen_signal: float = 0.5
    spermatogenic_activity: float = 0.5
    reproductive_capacity: float = 0.5

    def step(self, dt: float, gonadal_drive: float = 0.5) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        drive = max(0.0, min(1.0, float(gonadal_drive)))
        self.gonadal_activity = max(0.0, min(1.0, 0.85 * self.gonadal_activity + 0.15 * drive))
        self.androgen_signal = max(0.0, min(1.0, 0.8 * self.androgen_signal + 0.2 * self.gonadal_activity))
        self.spermatogenic_activity = max(0.0, min(1.0, self.spermatogenic_activity + 0.01 * self.gonadal_activity * dt / 3600.0))
        self.spermatogenic_activity = min(1.0, max(0.0, self.spermatogenic_activity - 0.005 * (1.0 - self.gonadal_activity) * dt / 3600.0))
        self.reproductive_capacity = max(
            0.0,
            min(1.0, 0.6 * self.reproductive_capacity + 0.4 * self.spermatogenic_activity),
        )
        return {
            "gonadal_activity": self.gonadal_activity,
            "androgen_signal": self.androgen_signal,
            "spermatogenic_activity": self.spermatogenic_activity,
            "reproductive_capacity": self.reproductive_capacity,
        }
