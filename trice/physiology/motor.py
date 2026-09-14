"""Musculoskeletal and motor-control abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MotorModel:
    posture: float = 0.0
    balance: float = 1.0
    fatigue: float = 0.0
    proprioception: float = 1.0
    movement: float = 0.0

    def step(self, dt: float, command: float = 0.0, sensory_error: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        command = max(-1.0, min(1.0, float(command)))
        sensory_error = max(0.0, min(1.0, float(sensory_error)))
        control = command * (1.0 - 0.5 * self.fatigue) + 0.25 * (0.5 - self.posture)
        self.movement += (control - self.movement) * min(1.0, dt * 2.0)
        self.posture += self.movement * dt * 0.1
        self.balance += ((1.0 - sensory_error) - self.balance) * min(1.0, dt * 0.8)
        self.fatigue += (abs(self.movement) * 0.12 - self.fatigue * 0.06) * dt
        self.fatigue = max(0.0, min(1.0, self.fatigue))
        self.proprioception = max(0.0, min(1.0, 1.0 - 0.35 * self.fatigue))
        return {
            "motor_posture": self.posture,
            "motor_balance": self.balance,
            "motor_fatigue": self.fatigue,
            "proprioception": self.proprioception,
            "movement": self.movement,
        }
