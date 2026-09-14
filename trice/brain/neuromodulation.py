"""Neuromodulator state channels for adaptive neural control."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Neuromodulators:
    dopamine: float = 0.5
    serotonin: float = 0.5
    endorphins: float = 0.5
    noradrenaline: float = 0.5
    acetylcholine: float = 0.5

    def step(self, dt: float, reward: float = 0.0, threat: float = 0.0, attention: float = 0.5, pain: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        reward = max(-1.0, min(1.0, float(reward)))
        threat = max(0.0, min(1.0, float(threat)))
        attention = max(0.0, min(1.0, float(attention)))
        pain = max(0.0, min(1.0, float(pain)))
        targets = {
            "dopamine": 0.5 + 0.35 * reward,
            "serotonin": 0.55 - 0.15 * threat,
            "endorphins": 0.5 + 0.35 * pain,
            "noradrenaline": 0.5 + 0.45 * threat,
            "acetylcholine": 0.45 + 0.45 * attention,
        }
        for key, target in targets.items():
            current = getattr(self, key)
            setattr(self, key, current + (target - current) * min(1.0, dt * 0.7))
        return {
            "dopamine": self.dopamine,
            "serotonin": self.serotonin,
            "endorphins": self.endorphins,
            "noradrenaline": self.noradrenaline,
            "acetylcholine": self.acetylcholine,
        }
