"""Whole-body movement and posture state."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MusculoskeletalState:
    muscle_activation: float = 0.0
    joint_stability: float = 1.0
    fatigue: float = 0.0
    balance: float = 1.0
    posture: float = 1.0

    def step(self, dt: float, command: float = 0.0, load: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        command = max(-1.0, min(1.0, float(command)))
        load = max(0.0, float(load))
        self.muscle_activation = 0.8 * self.muscle_activation + 0.2 * abs(command)
        self.fatigue = max(0.0, min(1.0, self.fatigue + load * dt - 0.02 * dt))
        self.balance = max(0.0, min(1.0, self.balance - 0.1 * abs(command) * dt))
        self.posture = max(0.0, min(1.0, 1.0 - self.fatigue * 0.25))
        return {
            "muscle_activation": self.muscle_activation,
            "joint_stability": self.joint_stability,
            "musculoskeletal_fatigue": self.fatigue,
            "balance": self.balance,
            "posture": self.posture,
        }
