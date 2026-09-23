"""Detailed female reproductive state surface.

This module represents explicit physiological variables for simulation; it is
not a clinically validated reproductive model.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FemaleReproductiveState:
    ovarian_activity: float = 0.5
    estrogen_signal: float = 0.5
    progesterone_signal: float = 0.5
    uterine_state: float = 0.5
    cycle_phase: float = 0.0

    def step(self, dt: float, gonadal_drive: float = 0.5) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        drive = max(0.0, min(1.0, float(gonadal_drive)))
        self.cycle_phase = (self.cycle_phase + dt / (28.0 * 86400.0)) % 1.0
        phase_signal = 0.5 + 0.5 * __import__("math").sin(self.cycle_phase * 2.0 * __import__("math").pi)
        self.ovarian_activity = max(0.0, min(1.0, 0.8 * self.ovarian_activity + 0.2 * (0.5 * drive + 0.5 * phase_signal)))
        self.estrogen_signal = max(0.0, min(1.0, 0.8 * self.estrogen_signal + 0.2 * self.ovarian_activity))
        self.progesterone_signal = max(0.0, min(1.0, 0.85 * self.progesterone_signal + 0.15 * (1.0 - abs(self.cycle_phase - 0.5) * 2.0)))
        self.uterine_state = max(0.0, min(1.0, 0.8 * self.uterine_state + 0.2 * self.progesterone_signal))
        return {
            "ovarian_activity": self.ovarian_activity,
            "estrogen_signal": self.estrogen_signal,
            "progesterone_signal": self.progesterone_signal,
            "uterine_state": self.uterine_state,
            "reproductive_cycle_phase": self.cycle_phase,
        }
