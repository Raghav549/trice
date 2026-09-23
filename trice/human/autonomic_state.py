"""Autonomic regulation state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AutonomicState:
    sympathetic: float = 0.5
    parasympathetic: float = 0.5
    baroreflex: float = 0.5
    arousal: float = 0.5

    def step(self, dt: float, stress: float = 0.0, relaxation: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        stress = max(0.0, min(1.0, float(stress)))
        relaxation = max(0.0, min(1.0, float(relaxation)))
        self.sympathetic = max(0.0, min(1.0, 0.8 * self.sympathetic + 0.2 * stress))
        self.parasympathetic = max(0.0, min(1.0, 0.8 * self.parasympathetic + 0.2 * relaxation))
        self.baroreflex = max(0.0, min(1.0, 0.9 * self.baroreflex + 0.1 * (1.0 - stress)))
        self.arousal = max(0.0, min(1.0, 0.5 + 0.5 * self.sympathetic - 0.3 * self.parasympathetic))
        return {
            "sympathetic_tone": self.sympathetic,
            "parasympathetic_tone": self.parasympathetic,
            "baroreflex": self.baroreflex,
            "autonomic_arousal": self.arousal,
        }
