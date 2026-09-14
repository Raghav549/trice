"""Digestive tract and nutrient absorption abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DigestionModel:
    gastric: float = 0.0
    intestinal: float = 0.0
    absorption: float = 0.0
    liver_processing: float = 0.0
    pancreatic_output: float = 0.0
    gut_motility: float = 0.5

    def step(self, dt: float, food: float = 0.0, stress: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        food = max(0.0, min(1.0, float(food)))
        stress = max(0.0, min(1.0, float(stress)))
        self.gastric += (food - self.gastric) * min(1.0, dt * 0.7)
        transit = max(0.0, self.gut_motility * (1.0 - 0.35 * stress))
        self.intestinal += (self.gastric - self.intestinal) * min(1.0, dt * transit)
        self.absorption += (self.intestinal - self.absorption) * min(1.0, dt * 0.5)
        self.pancreatic_output = max(0.0, min(1.0, self.intestinal * 0.9))
        self.liver_processing += (self.absorption - self.liver_processing) * min(1.0, dt * 0.4)
        self.gastric *= max(0.0, 1.0 - 0.12 * dt)
        return {
            "gastric_state": self.gastric,
            "intestinal_state": self.intestinal,
            "nutrient_absorption": self.absorption,
            "liver_processing": self.liver_processing,
            "pancreatic_output": self.pancreatic_output,
            "gut_motility": self.gut_motility,
        }
