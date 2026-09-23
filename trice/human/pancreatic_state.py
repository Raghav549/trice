"""Pancreatic endocrine/exocrine state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PancreaticState:
    insulin: float = 0.5
    glucagon: float = 0.5
    digestive_enzyme_output: float = 0.5

    def step(self, dt: float, glucose: float = 0.5, food: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        glucose = max(0.0, min(1.0, float(glucose)))
        food = max(0.0, min(1.0, float(food)))
        self.insulin = max(0.0, min(1.0, 0.8 * self.insulin + 0.2 * glucose))
        self.glucagon = max(0.0, min(1.0, 0.8 * self.glucagon + 0.2 * (1.0 - glucose)))
        self.digestive_enzyme_output = max(0.0, min(1.0, 0.8 * self.digestive_enzyme_output + 0.2 * food))
        return {
            "pancreatic_insulin": self.insulin,
            "pancreatic_glucagon": self.glucagon,
            "digestive_enzyme_output": self.digestive_enzyme_output,
        }
