"""Homeostatic drive generation from internal state."""
from __future__ import annotations

from dataclasses import dataclass

from .behavior import BehavioralState
from .internal_state import InternalState


@dataclass
class DriveModel:
    sensitivity: float = 1.0

    def update(self, internal: InternalState, drives: BehavioralState) -> BehavioralState:
        if self.sensitivity < 0:
            raise ValueError("sensitivity cannot be negative")
        drives.hunger = max(0.0, min(1.0, self.sensitivity * max(0.0, 0.6 - internal.glucose)))
        drives.thirst = max(0.0, min(1.0, self.sensitivity * max(0.0, 1.0 - internal.hydration)))
        drives.fatigue = max(0.0, min(1.0, self.sensitivity * max(0.0, 1.0 - internal.body_energy)))
        drives.pain = getattr(drives, "pain", 0.0)
        return drives
