"""Behavioral state surface combining drives and action intent."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BehavioralState:
    hunger: float = 0.0
    thirst: float = 0.0
    fatigue: float = 0.0
    curiosity: float = 0.0
    threat: float = 0.0
    social_drive: float = 0.0

    def clamp(self) -> None:
        for name in ("hunger", "thirst", "fatigue", "curiosity", "threat", "social_drive"):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))
