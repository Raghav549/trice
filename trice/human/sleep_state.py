"""Sleep-wake and circadian state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SleepState:
    circadian_phase: float = 0.5
    sleep_pressure: float = 0.0
    awake: bool = True
    alertness: float = 1.0

    def step(self, dt: float, sleep_input: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.sleep_pressure = max(0.0, min(1.0, self.sleep_pressure + (0.08 if self.awake else -0.12) * dt))
        requested_sleep = float(sleep_input) > 0.5
        self.awake = not requested_sleep
        self.alertness = max(0.0, min(1.0, 1.0 - self.sleep_pressure + (0.2 if self.awake else -0.1)))
        self.circadian_phase = (self.circadian_phase + dt / 86400.0) % 1.0
        return {
            "circadian_phase": self.circadian_phase,
            "sleep_pressure": self.sleep_pressure,
            "awake": 1.0 if self.awake else 0.0,
            "alertness": self.alertness,
        }
