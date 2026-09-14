"""Skin-barrier and thermoregulation abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IntegumentaryModel:
    skin_barrier: float = 1.0
    core_temperature: float = 1.0
    sweating: float = 0.0
    vasomotor_tone: float = 0.5
    pain_sensitivity: float = 0.5

    def step(self, dt: float, ambient: float = 1.0, activity: float = 0.0, pain: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        ambient = max(0.0, min(2.0, float(ambient)))
        activity = max(0.0, min(1.0, float(activity)))
        pain = max(0.0, min(1.0, float(pain)))
        heat_load = 0.04 * activity + 0.01 * (ambient - 1.0)
        self.core_temperature += (heat_load + (1.0 - self.core_temperature) * 0.08) * dt
        deviation = self.core_temperature - 1.0
        self.sweating = max(0.0, min(1.0, deviation * 2.5))
        self.vasomotor_tone += ((0.5 - 0.4 * deviation) - self.vasomotor_tone) * min(1.0, dt * 0.4)
        self.pain_sensitivity += (pain - self.pain_sensitivity) * min(1.0, dt * 0.8)
        self.skin_barrier = max(0.0, min(1.0, self.skin_barrier - 0.001 * pain * dt))
        return {
            "skin_barrier": self.skin_barrier,
            "core_temperature": self.core_temperature,
            "sweating": self.sweating,
            "vasomotor_tone": self.vasomotor_tone,
            "pain_sensitivity": self.pain_sensitivity,
        }
