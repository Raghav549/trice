"""Gut-microbiome-facing metabolic interface abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MicrobiomeModel:
    diversity: float = 0.8
    metabolic_output: float = 0.5
    barrier_support: float = 0.8
    inflammatory_signal: float = 0.1

    def step(self, dt: float, fiber_input: float = 0.0, stress: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        fiber_input = max(0.0, min(1.0, float(fiber_input)))
        stress = max(0.0, min(1.0, float(stress)))
        self.diversity += (0.8 + 0.15 * fiber_input - 0.2 * stress - self.diversity) * min(1.0, dt * 0.15)
        self.metabolic_output += (0.25 + 0.55 * self.diversity * fiber_input - self.metabolic_output) * min(1.0, dt * 0.25)
        self.barrier_support += (self.diversity - self.barrier_support) * min(1.0, dt * 0.2)
        self.inflammatory_signal += (stress * 0.3 - self.inflammatory_signal * 0.4) * dt
        self.diversity = max(0.0, min(1.0, self.diversity))
        self.barrier_support = max(0.0, min(1.0, self.barrier_support))
        self.inflammatory_signal = max(0.0, min(1.0, self.inflammatory_signal))
        return {
            "microbiome_diversity": self.diversity,
            "microbial_metabolic_output": self.metabolic_output,
            "gut_barrier_support": self.barrier_support,
            "microbial_inflammation": self.inflammatory_signal,
        }
