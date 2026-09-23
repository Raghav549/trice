"""Peripheral and central nervous-system state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NervousState:
    sensory_gain: float = 1.0
    motor_drive: float = 0.0
    neural_arousal: float = 0.5
    signal_fidelity: float = 1.0
    reflex_readiness: float = 0.5

    def step(self, dt: float, sensory_load: float = 0.0, threat: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        sensory_load = max(0.0, min(1.0, float(sensory_load)))
        threat = max(0.0, min(1.0, float(threat)))
        self.neural_arousal = max(0.0, min(1.0, 0.8 * self.neural_arousal + 0.2 * max(sensory_load, threat)))
        self.sensory_gain = max(0.0, min(2.0, 0.8 + 0.4 * self.neural_arousal))
        self.motor_drive = max(-1.0, min(1.0, 0.5 * threat))
        self.signal_fidelity = max(0.0, min(1.0, 1.0 - 0.2 * threat))
        self.reflex_readiness = max(0.0, min(1.0, 0.5 + 0.5 * self.neural_arousal))
        return {
            "sensory_gain": self.sensory_gain,
            "motor_drive": self.motor_drive,
            "neural_arousal": self.neural_arousal,
            "signal_fidelity": self.signal_fidelity,
            "reflex_readiness": self.reflex_readiness,
        }
