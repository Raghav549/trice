"""Liver metabolic-processing state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HepaticState:
    glycogen: float = 0.5
    detox_load: float = 0.0
    protein_processing: float = 0.5
    bile_output: float = 0.5

    def step(self, dt: float, nutrient_load: float = 0.0, toxin_load: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        nutrient_load = max(0.0, min(1.0, float(nutrient_load)))
        toxin_load = max(0.0, min(1.0, float(toxin_load)))
        self.glycogen = max(0.0, min(1.0, self.glycogen + 0.1 * nutrient_load * dt - 0.05 * dt))
        self.detox_load = max(0.0, min(1.0, 0.9 * self.detox_load + 0.1 * toxin_load))
        self.protein_processing = max(0.0, min(1.0, 0.5 + 0.4 * nutrient_load))
        self.bile_output = max(0.0, min(1.0, 0.5 + 0.2 * nutrient_load))
        return {
            "hepatic_glycogen": self.glycogen,
            "hepatic_detox_load": self.detox_load,
            "hepatic_protein_processing": self.protein_processing,
            "bile_output": self.bile_output,
        }
