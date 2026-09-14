"""Reproductive/endocrine state abstraction for life-cycle simulation."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReproductiveModel:
    developmental_state: float = 0.5
    reproductive_signal: float = 0.5
    gonadal_state: float = 0.5
    cycle_phase: float = 0.0

    def step(self, dt: float, endocrine_signal: float = 0.5, development: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        endocrine_signal = max(0.0, min(1.0, float(endocrine_signal)))
        development = max(0.0, min(1.0, float(development)))
        self.developmental_state += (development - self.developmental_state) * min(1.0, dt * 0.02)
        self.reproductive_signal += (endocrine_signal - self.reproductive_signal) * min(1.0, dt * 0.2)
        self.gonadal_state += (self.reproductive_signal - self.gonadal_state) * min(1.0, dt * 0.08)
        self.cycle_phase = (self.cycle_phase + dt * 0.01) % 1.0
        return {
            "developmental_state": self.developmental_state,
            "reproductive_signal": self.reproductive_signal,
            "gonadal_state": self.gonadal_state,
            "cycle_phase": self.cycle_phase,
        }
