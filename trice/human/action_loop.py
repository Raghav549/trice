"""Perception -> internal state -> drives -> mind -> action pipeline."""
from __future__ import annotations

from dataclasses import dataclass, field

from .behavior import BehavioralState
from .drive_model import DriveModel
from .internal_state import InternalState
from .mind import MindState
from .sensory_fusion import fuse


@dataclass
class HumanActionLoop:
    internal: InternalState = field(default_factory=InternalState)
    behavior: BehavioralState = field(default_factory=BehavioralState)
    mind: MindState = field(default_factory=MindState)
    drives: DriveModel = field(default_factory=DriveModel)

    def step(self, senses: dict[str, float]) -> dict[str, float]:
        attention = fuse(senses, self.mind.attention)
        self.behavior = self.drives.update(self.internal, self.behavior)
        self.mind.attention = attention
        self.mind.goal_pressure = max(
            self.behavior.hunger,
            self.behavior.thirst,
            self.behavior.fatigue,
            self.behavior.threat,
        )
        self.mind.clamp()
        movement = max(-1.0, min(1.0, self.mind.goal_pressure - self.mind.threat if hasattr(self.mind, "threat") else self.mind.goal_pressure))
        return {"movement": movement, "attention": self.mind.attention}
