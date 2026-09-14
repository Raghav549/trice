"""Slow hormonal control channels and feedback regulation."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EndocrineAxes:
    cortisol: float = 0.2
    insulin: float = 0.5
    thyroid_signal: float = 0.5
    growth_signal: float = 0.5
    reproductive_signal: float = 0.5
    circadian_signal: float = 0.5

    def step(self, dt: float, stress: float = 0.0, glucose: float = 1.0, circadian: float = 0.5) -> dict[str, float]:
        dt = max(0.0, float(dt))
        stress = max(0.0, min(1.0, float(stress)))
        glucose = max(0.0, min(2.0, float(glucose)))
        circadian = max(0.0, min(1.0, float(circadian)))
        targets = {
            "cortisol": 0.15 + 0.75 * stress,
            "insulin": max(0.0, min(1.0, glucose / 2.0)),
            "thyroid_signal": 0.45 + 0.2 * (1.0 - stress),
            "growth_signal": 0.5 + 0.15 * (1.0 - self.cortisol),
            "reproductive_signal": 0.5 * (1.0 - 0.4 * stress),
            "circadian_signal": circadian,
        }
        for name, target in targets.items():
            current = getattr(self, name)
            setattr(self, name, current + (target - current) * min(1.0, dt * 0.25))
        return {
            "cortisol": self.cortisol,
            "insulin": self.insulin,
            "thyroid_signal": self.thyroid_signal,
            "growth_signal": self.growth_signal,
            "reproductive_signal": self.reproductive_signal,
            "circadian_signal": self.circadian_signal,
        }
