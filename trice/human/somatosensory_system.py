"""Touch, pressure, temperature and pain perception surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SomatosensorySystem:
    touch: float = 0.0
    pressure: float = 0.0
    temperature: float = 0.5
    pain: float = 0.0
    proprioception: float = 0.5

    def ingest(
        self,
        touch: float = 0.0,
        pressure: float = 0.0,
        temperature: float = 0.5,
        pain: float = 0.0,
        proprioception: float = 0.5,
    ) -> dict[str, float]:
        self.touch = max(0.0, min(1.0, abs(float(touch))))
        self.pressure = max(0.0, min(1.0, abs(float(pressure))))
        self.temperature = max(0.0, min(1.0, float(temperature)))
        self.pain = max(0.0, min(1.0, float(pain)))
        self.proprioception = max(0.0, min(1.0, float(proprioception)))
        return {
            "touch_signal": self.touch,
            "pressure_signal": self.pressure,
            "skin_temperature_signal": self.temperature,
            "pain_signal": self.pain,
            "proprioception_signal": self.proprioception,
        }
